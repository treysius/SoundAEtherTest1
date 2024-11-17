import configparser
import threading

import configUtil
import os.path
from random import randrange
from socket import *

import databaseUtil

#load config
config = configUtil.load_config('config.ini')

#check if database exists
databaseUtil.db_exists(config.get('Database', 'db_filename'))

#create socket to listen on
s = socket()
portNum = config.getint('Connections', 'server_port')
s.bind(("", portNum))
print("server listening")
s.listen()

#listen for incoming connections
while True:
    c, a = s.accept()
    print("connection established with ip "+a[1])

    #determine what the client wants and respond accordingly
    d = c.recv(1024).decode()
    #'data' for get data
    #'stream 3' for stream song with id 3
    data = d.split(" ")
    match data[0]:
        case 'data':
            c.send(databaseUtil.get_data(config.get('Database', 'db_filename')))
        case 'stream':
            threading.Thread(target=databaseUtil.stream_audio,args=(data[1], c)).start()



