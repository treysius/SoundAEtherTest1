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
            Id INTEGER PRIMARY KEY,
            Name TEXT,
            Artist TEXT,
            Album TEXT,
            Release_Date TEXT,
            Cover_IMG BLOB);"""
            playlistTable = """CREATE TABLE PLAYLISTS (
            Id INTEGER PRIMARY KEY,
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

    #will send the client all song and playlist data in the database
    def get_data(self, s: socket.socket):

        ts = self.data_to_string()
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
        fc = s.recv(chunk).decode()
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
        cursor.execute("""SELECT Id FROM SONGS ORDER BY Id DESC LIMIT 1""")
        conn.commit()
        sid = cursor.fetchone()[0]

        #name audio file
        os.rename(self.audio_dirname+"temp.wav", self.audio_dirname+str(sid)+".wav")

        cursor.close()
        conn.close()

        return 1

    def add_playlist(self, name:"", sids:list[int]):
        conn = sqlite3.connect(self.db_filename)
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO PLAYLISTS (Name, Song_Ids) VALUES (?, ?)""", (name, json.dumps(sids)))
        conn.commit()
        cursor.close()
        conn.close()
        return

    def edit_playlist(self, id:int, sids:list[int]):
        conn = sqlite3.connect(self.db_filename)
        cursor = conn.cursor()
        cursor.execute("""UPDATE PLAYLISTS SET Song_Ids = ? WHERE Id = ?""", (json.dumps(sids), id))
        conn.commit()
        cursor.close()
        conn.close()
        return

    def remove_song(self, id:int):
        conn = sqlite3.connect(self.db_filename)
        cursor = conn.cursor()
        cursor.execute("""DELETE FROM SONGS WHERE Id = ?""", (id,))
        conn.commit()
        cursor.close()
        conn.close()
        os.remove(str(self.audio_dirname+str(id)+".wav"))
        return

    def remove_playlist(self, id:int):
        conn = sqlite3.connect(self.db_filename)
        cursor = conn.cursor()
        cursor.execute("""DELETE FROM PLAYLISTS WHERE Id = ?""", (id,))
        conn.commit()
        cursor.close()
        conn.close()
        return

    def data_to_string(self) -> str:
        #get data
        conn = sqlite3.connect(self.db_filename)
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM SONGS""")
        sdata = cursor.fetchall()
        cursor.execute("""SELECT * FROM PLAYLISTS""")
        pdata = cursor.fetchall()
        cursor.close()
        conn.close()


        return str(sdata)+str(pdata)