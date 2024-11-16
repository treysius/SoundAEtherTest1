# Big thanks to Pyshine for the basic code for recieving
# audio over TCP
# Their code can be found here:
# https://pyshine.com/How-to-send-audio-from-PyAudio-over-socket/
# This is server code to receive video and audio frames over TCP
# 

import socket
import threading, wave, pyaudio,pickle,struct,os,sys,time
import sqlite3

host_name = socket.gethostname()
host_ip = '192.168.86.31'#  socket.gethostbyname(host_name)
print(host_ip)
port = 9611

con = sqlite3.connect("SongTest.db")


cur = con.cursor()

res = cur.execute("Select * FROM Playlist1")
endsong = 0
for row in res:
    print(row)
    endsong += 1

global startsong
startsong = int(input("Select the number of the song you wish to listen to..."))

res = cur.execute(f"Select songfile FROM Playlist1 WHERE songindex={startsong}")

filename =  "".join(res.fetchone())
command = "cd\\ && cd Users\\treys\\PythonTestServer && ffmpeg -i {} -ab 160k -ac 2 -ar 44100 -vn {} -y".format(filename,'temp.wav')
os.system(command)
con.close()

def audio_stream():
    global startsong
    server_socket = socket.socket()
    server_socket.bind((host_ip, (port-1)))

    server_socket.listen(5)
    CHUNK = 1024
    wf = wave.open("temp.wav", 'rb')
    
    p = pyaudio.PyAudio()
    print('server listening at',(host_ip, (port-1)))
   
    
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    input=True,
                    frames_per_buffer=CHUNK)

             

    client_socket,addr = server_socket.accept()
 
    data = data = wf.readframes(CHUNK)
    while True:
        if client_socket:
            while True:
              
                #data = wf.readframes(CHUNK)
                if data !='':
                    a = pickle.dumps(data)
                    message = struct.pack("Q",len(a))+a
                    client_socket.sendall(message)

                    data = wf.readframes(CHUNK)
                if data == b'':
                    #client_socket.close()
                    print("end of song")
                    time.sleep(5)
                    if startsong==endsong-1:
                        client_socket.close()
                        
                        break

                    con = sqlite3.connect("SongTest.db")
                    cur = con.cursor()
                    
                    startsong = startsong+1

                    res = cur.execute(f"Select songfile FROM Playlist1 WHERE songindex={startsong}")

                    filename =  "".join(res.fetchone())
                    command = "cd\\ && cd Users\\treys\\PythonTestServer && ffmpeg -i {} -ab 160k -ac 2 -ar 44100 -vn {} -y".format(filename,'temp.wav')
                    os.system(command)
                    con.close()
                    wf.rewind()
                    data = wf.readframes(CHUNK)
        break
                
t1 = threading.Thread(target=audio_stream, args=())
t1.start()




