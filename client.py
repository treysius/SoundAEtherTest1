from socket import *
import json


#check if server address file exists

#if server address file exists, get server ip and port from there, otherwise, ask the user for it and make the file


ip = input("enter the ip address to connect to(or -1 for localhost)")
if ip == "-1":
    ip = '127.0.0.1'
port = input("enter the port number to connect to")

# create socket connection
s = socket()
s.connect((ip, int(port)))

#get song and playlist data
ts = "data"
s.send(ts.encode())

data = s.recv(1024).decode()

#data should be a json, turn it into useful data and display to user