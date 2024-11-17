import json
import os.path
import socket
import sqlite3
import wave
import pyaudio

#will return all song and playlist data except the audio in the database
def get_data(filename: "") -> "":
    data = {'songs': {'Id': '1','Name': 'testsong', 'Artist': 'testartist', 'Release_Date': 'testdate'}, 'playlists': {'Id': '1', 'Name': 'testplaylist', 'song_Ids': '1' }}

    return data

#will stream the song audio to the specified socket
def stream_audio(songid: int, s: socket.socket):
    chunk = 1024

    #load file
    f = wave.open(str(songid)+r".wav", "rb")

    pya = pyaudio.PyAudio()

    stream = pya.open(format = pya.get_format_from_width(f.getsampwidth()),
                      channels=f.getnchannels(),
                      rate=f.getframerate(),
                      output=True)

    data = f.readframes(chunk)

    while data:
        stream.write(data)
        data = f.readframes(chunk)

    stream.stop_stream()
    stream.close()
    pya.terminate()

    return

def db_exists(filename:""):
    #if database does not exist, create a blank one
    if not os.path.isfile(filename):
        con = sqlite3.connect(filename)
        cursor = con.cursor()
        songTable = """ CREATE TABLE SONGS (
        Id INT
        Name TEXT
        Artist TEXT
        Album TEXT
        Release_Date TEXT
        Cover_IMG BLOB
        Audio BLOB);"""
        playlistTable = """CREATE TABLE PLAYLISTS (
        Id INT
        Name TEXT
        Song_Ids TEXT);"""
        cursor.execute(songTable)
        cursor.execute(playlistTable)