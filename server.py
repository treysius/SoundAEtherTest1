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
    databaseUtil.db_exists(config.get('Database', 'db_filename'))

    #menu to add songs and playlists
    choice = '0'
    while not choice == "6":
        choice = input("1. add new song\n"
                       "2. add new playlist\n"
                       "3. edit playlist\n"
                       "4. remove song\n"
                       "5. remove playlist\n"
                       "6. start server\n"
                       "7. exit\n"
                       "Choose an option")
        match choice:
            case "7":
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
                ts = json.dumps(databaseUtil.get_data(config.get('Database', 'db_filename')),indent=4)
                c.send(ts.encode())
                c.close()
            case 'stream':
                threading.Thread(target=databaseUtil.stream_audio,args=(data[1], c)).start()

if __name__=="__main__":
    main()

