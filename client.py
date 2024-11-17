import os.path
from socket import *
import json

#variables
serverIP = ""
serverPort = ""

#if server address file exists, get server ip and port from there, otherwise, ask the user for it and make the file
filename = "serverAddress.txt"
if os.path.isfile(filename):
    with open(filename, "r") as file:
        serverIP = file.readline()
        serverPort = file.readline()

else:
    serverIP = input("enter the ip address to connect to(or -1 for localhost)")
    if serverIP == "-1":
        serverIP = '127.0.0.1'
    serverPort = input("enter the port number to connect to")


#menu for user to control the program
while True:
    choice = input("1. get song and playlist data\n" +
          "2. stream song\n" +
          "3. exit\n" +
          "Choose an option")

    match choice:
        case "1":
            #connect to server
            s = socket()
            s.connect((serverIP,int(serverPort)))

            #get data
            ts = "data"
            s.send(ts.encode())
            data = s.recv(1024).decode()
            print(data)
            s.close()

        case "2":
            songID = input("enter the song id to play")
            # connect to server
            s = socket()
            s.connect((serverIP, int(serverPort)))


            #start stream
            ts = "stream "+str(songID)
            s.send(ts.encode())

        case "3":
            break


