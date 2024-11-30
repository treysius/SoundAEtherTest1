import datetime
import json
import os.path
import socket
import sqlite3
import wave
import shutil
from PIL import Image


class DB_Util:
    def __init__(self, db_filename: "", audio_dirname: ""):
        self.db_filename = db_filename
        # if database does not exist, create a blank one
        if not os.path.isfile(db_filename):
            con = sqlite3.connect(db_filename)
            cursor = con.cursor()
            songTable = """ CREATE TABLE SONGS (
            Name TEXT,
            Artist TEXT,
            Album TEXT,
            Release_Date TEXT,
            Cover_IMG BLOB);"""
            playlistTable = """CREATE TABLE PLAYLISTS (
            Name TEXT,
            Song_Ids TEXT);"""
            cursor.execute(songTable)
            cursor.execute(playlistTable)
            cursor.close()
            con.close()

        # if audio folder does not exist, make it
        current = os.getcwd()
        self.audio_dirname = os.path.join(current, audio_dirname)+"/"
        if not os.path.isdir(audio_dirname):
            os.mkdir(audio_dirname)

    #will return all song and playlist data except the audio in the database
    def get_data(self, s: socket.socket):
        #get data
        conn = sqlite3.connect(self.db_filename)
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM SONGS""")
        data = cursor.fetchall()
        cursor.close()
        conn.close()

        ts = json.dumps(str(data), indent=4)
        s.sendall(ts.encode())

        return

    #will stream the song audio to the specified socket
    def stream_audio(self, songid: int, s: socket.socket):
        chunk = 1024

        #load file
        f = wave.open(self.audio_dirname+str(songid)+r".wav", "rb")

        #send client audio details
        ad = {'sampwidth':str(f.getsampwidth()),'channels':str(f.getnchannels()),'rate':str(f.getframerate())}
        ts = json.dumps(ad)
        s.send(ts.encode())

        #wait for client to be ready for audio
        fc = s.recv(1024).decode()
        if fc==0:
            return

        #send audio
        data = f.readframes(chunk)
        while data:
            s.send(data)
            data = f.readframes(chunk)

        s.close()
        return

    #adds a song to the database, returns 1 on success, or 0 on failure
    def add_song(self, audioFile:"", name:"", artist:"", album:"", releaseDate:"", coverIMG:"") -> int:
        #make sure the files exist
        if not os.path.isfile(audioFile):
            return 0
        if not (coverIMG == "-1" or os.path.isfile(coverIMG)):
            return 0

        #make sure the file types are correct
        if not audioFile[len(audioFile) - 4:] == ".wav":
            return 0
        if not coverIMG == "-1":
            if not coverIMG[len(coverIMG) - 4:] == ".jpg":
                return 0

        conn = sqlite3.connect(self.db_filename)
        cursor = conn.cursor()

        #get cover image bytes
        if coverIMG == "-1":
            imgBytes = "-1".encode()
        else:
            img = Image.open(coverIMG)
            img = img.convert("RGB")
            img.thumbnail((500, 500))
            imgBytes = img.tobytes()

        #move audio file
        shutil.copyfile(audioFile, self.audio_dirname+"temp.wav")

        #add to database
        cursor.execute("""INSERT INTO SONGS (Name, Artist, Album, Release_Date, Cover_IMG) VALUES (?, ?, ?, ?, ?)""", (name, artist,album, releaseDate, imgBytes))
        #get song id
        cursor.execute("""SELECT rowid FROM SONGS ORDER BY rowid DESC LIMIT 1""")
        conn.commit()
        sid = cursor.fetchone()[0]

        #name audio file
        os.rename(self.audio_dirname+"temp.wav", self.audio_dirname+str(sid)+".wav")

        cursor.close()
        conn.close()

        return 1

    def add_playlist(self):
        return

    def edit_playlist(self):
        return

    def remove_song(self):
        return

    def remove_playlist(self):
        return
