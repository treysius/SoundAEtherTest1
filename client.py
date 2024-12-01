import os.path
from socket import *
import json
import pyaudio


def main():
    #variables

    #if server address file exists, get server ip and port from there, otherwise, ask the user for it and make the file
    filename = "serverAddress.txt"
    if os.path.isfile(filename):
        with open(filename, "r") as file:
            serverIP = file.readline().strip("\n")
            serverPort = file.readline()

    else:
        serverIP = input("enter the ip address to connect to(or -1 for localhost)")
        if serverIP == "-1":
            serverIP = "127.0.0.1"
        serverPort = input("enter the port number to connect to")
        with open(filename, "w") as file:
            file.write(serverIP+"\n"+serverPort)



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
                while not data:
                    data = s.recv(1024).decode()
                print(data)
                s.close()

            case "2":
                songID = input("enter the song id to play")
                # connect to server
                s = socket(AF_INET, SOCK_STREAM)
                s.connect((serverIP, int(serverPort)))

                #start stream
                ts = "stream "+str(songID)
                s.send(ts.encode())

                #wait for audio details
                fromServer = s.recv(1024).decode()
                while not fromServer:
                    fromServer = s.recv(1024).decode()
                ad = json.loads(fromServer)

                #load pyaudio
                pya = pyaudio.PyAudio()
                stream = pya.open(format=pya.get_format_from_width(int(ad['sampwidth'])),
                                  channels=int(ad['channels']),
                                  rate=int(ad['rate']),
                                  output=True)

                #ready for audio
                s.send("1".encode())

                #eventually add some error detection and send the server 0 if there is an error

                #play audio
                print("playing audio")
                data = s.recv(1024)
                while data:
                    stream.write(data)
                    data = s.recv(1024)

                #cleanup
                stream.stop_stream()
                stream.close()
                pya.terminate()
                s.close()


            case "3":
                break
if __name__=="__main__":
    main()

