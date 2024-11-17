import json
import os.path
import socket
import pyflac
import sqlite3

#will return all song and playlist data except the audio in the database
def get_data(filename: "") -> json:
    con = sqlite3.connect(filename)
    return json

#will stream the song audio to the specified socket
def stream_audio(songid: int, s: socket.socket):
    s.send("test")
    return

def db_exists(filename:""):
    #if database does not exist, create a blank one
    if not os.path.isfile(filename):
        con = con = sqlite3.connect(filename)
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