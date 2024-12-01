import configparser
import json
import threading
import configUtil
from socket import *
import databaseUtil

def main():
    #load config

    config: configparser = configUtil.load_config('config.ini')

    #check if database exists
    db = databaseUtil.DB_Util(config.get('Database', 'db_filename'), config.get('Database', 'audio_dirname'))

    #menu to add songs and playlists
    choice = '0'
    while not choice == "7":
        choice = input("1. add new song\n"
                       "2. add new playlist\n"
                       "3. edit playlist\n"
                       "4. remove song\n"
                       "5. remove playlist\n"
                       "6. list data\n"
                       "7. start server\n"
                       "8. exit\n"
                       "Choose an option")
        match choice:
            case "1":
                db.add_song(input("enter the path to the audio file"), input("enter the name of the song"), input("enter the artist of the song"), input("enter the album of the song"), input("enter the release date of the song"), input("enter the path to the cover image of the song, or -1 if there is none"))

            case "2":
                name = input("enter the name of the playlist")
                sIdStr = input("enter the song ids for the playlist separated by a space")
                sIds = sIdStr.split()
                sidList = [ int(x) for x in sIds ]
                db.add_playlist(name, sidList)

            case "3":
                id = input("enter the id of the playlist")
                sIdStr = input("enter the new song ids for the playlist separated by a space")
                sIds = sIdStr.split()
                sidList = [int(x) for x in sIds]
                db.edit_playlist(id, sidList)

            case "4":
                sid = input("enter the id of the song")
                db.remove_song(int(sid))

            case "5":
                pid = input("enter the id of the playlist")
                db.remove_playlist(int(pid))

            case "6":
                print(db.data_to_string())

            case "8":
                return


    #create socket to listen on
    s = socket(AF_INET, SOCK_STREAM)
    portNum = config.getint('Connections', 'server_port')
    s.bind(("", portNum))
    print("server listening on port "+str(portNum))
    s.listen()

    #listen for incoming connections
    while True:
        c, a = s.accept()
        print("connection established with ip "+str(a[1]))

        #determine what the client wants and respond accordingly
        d = c.recv(1024).decode()
        #'data' for get data
        #'stream 3' for stream song with id 3
        data = d.split(" ")
        match data[0]:
            case 'data':

                threading.Thread(target=db.get_data, args=(c,)).start()
            case 'stream':
                threading.Thread(target=db.stream_audio,args=(data[1], c)).start()

if __name__=="__main__":
    main()

