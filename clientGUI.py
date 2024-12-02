from PyQt6.QtWidgets import QApplication
from PyQt6 import QtWidgets, QtGui
from PyQt6.QtCore import *
from SoundAetherUIElements import SoundAetherServerMenu, SoundAetherAddMenu, SoundAetherMainMenu, SoundAetherPlaylistMenu
import sys
from socket import *
import json
import os.path
import pyaudio
import time


PlaylistSel = ""

class ServerMenu(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(ServerMenu, self).__init__(parent)

        self.m_ui = SoundAetherServerMenu.Ui_Form()
        self.m_ui.setupUi(self)

        self.m_ui.ServerEnterButton.clicked.connect(self.EnterClicked)
    
    def EnterClicked(self):
        filename = "serverAddress.txt"
        serverIP = self.m_ui.ServerIDLineEdit.text()
        if serverIP == "-1":
            serverIP = "127.0.0.1"
        serverPort = self.m_ui.PortIDLineEdit.text()
        with open(filename, "w") as file:
            file.write(serverIP+"\n"+serverPort)
        self.close()
        runMainMenu()
        
        
        

class AddMenu(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(AddMenu, self).__init__(parent)

        self.m_ui = SoundAetherAddMenu.Ui_SAEMainMenu()
        self.m_ui.setupUi(self)

        self.m_ui.BackToPlaylistButton.clicked.connect(self.BackToPlaylistClicked)
        self.m_ui.DisconnectButton.clicked.connect(self.DisconnectButtonClicked)

    def BackToPlaylistClicked(self):
        self.close()
        mainwindow.show()
    def DisconnectButtonClicked(self):
        self.close()
        mainwindow.close()
        #playlistwindow.close()
        serverwindow.show()


class MainMenu(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MainMenu, self).__init__(parent)

        self.m_ui = SoundAetherMainMenu.Ui_SAEMainMenu()
        self.m_ui.setupUi(self)

        filename = "serverAddress.txt"
        if os.path.isfile(filename):
            with open(filename, "r") as file:
                serverIP = file.readline().strip("\n")
                serverPort = file.readline()
        
        self.m_ui.ServerIDLabel.setText(f"Connected to {serverIP}")

        #connect to server
        s = socket()
        s.connect((serverIP,int(serverPort)))

        #get data
        ts = "playlist"
        s.send(ts.encode())
        data = s.recv(1024).decode()
        while not data:
            data = s.recv(1024).decode()
        datastring = json.loads(data)
        datastring2 = "".join(datastring)
        datalist = datastring2.split(', ')
        datastring2 = "".join(datalist)
        datalist = datastring2.split("'")[1::2]
        print(datalist)

        self.m_ui.listWidget.addItems(datalist)

        self.m_ui.SelectPlaylistButton.clicked.connect(self.SelectClicked)
        self.m_ui.AddPlaylistButton.clicked.connect(self.AddPlaylistClicked)
        self.m_ui.AddSongButton.clicked.connect(self.AddSongClicked)
        self.m_ui.DisconnectButton.clicked.connect(self.DisconnectButtonClicked)


    def SelectClicked(self):
        0==0
        global PlaylistSel

        PlaylistName = [item.text() for item in self.m_ui.listWidget.selectedItems()]
        PlaylistSel = PlaylistName[0]
        global playlistwindow
        playlistwindow = PlaylistMenu()
        self.close()
        runPlaylistMenu()
    def AddPlaylistClicked(self):
        0==0
    def AddSongClicked(self):
        runAddMenu()
    def DisconnectButtonClicked(self):
        self.close()
        mainwindow.close()
        #playlistwindow.close()
        serverwindow.show()


class PlaylistMenu(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(PlaylistMenu, self).__init__(parent)

        self.m_ui = SoundAetherPlaylistMenu.Ui_SAEMainMenu()
        self.m_ui.setupUi(self)

        self.m_ui.PlaylistNumber.setText(PlaylistSel)

        filename = "serverAddress.txt"
        if os.path.isfile(filename):
            with open(filename, "r") as file:
                serverIP = file.readline().strip("\n")
                serverPort = file.readline()
        
        self.m_ui.ServerIDLabel.setText(f"Connected to {serverIP} on Port {serverPort}")

        self.threadpool = QThreadPool()

        #connect to server
        s = socket()
        s.connect((serverIP,int(serverPort)))

        #get data
        ts = "data"
        s.send(ts.encode())
        data = s.recv(1024).decode()
        while not data:
            data = s.recv(1024).decode()
        #print(json.loads(data))
        datastring = json.loads(data)
        datastring2 = "".join(datastring)[1:-1]
        datalist = datastring2.split(', ')
        #print(datalist)
        
        datalist = [datalist[n:n+7] for n in range(0, len(datalist), 7)]
        i = 0
        for item in datalist:
            #print(f"{item[6][1:-2]}")
            if PlaylistSel == item[6][1:-2]:
                self.m_ui.MusicList.addItem(f"{item[0][1:]} | {item[1][1:-1]} | {item[2][1:-1]}")
        s.close()

        self.m_ui.DisconnectButton.clicked.connect(self.DisconnectButtonClicked)
        self.m_ui.BackToPlaylistButton.clicked.connect(self.BackToPlaylistClicked)
        self.m_ui.StopSongButton.clicked.connect(self.StopSongClicked)
        self.m_ui.PlayButton.clicked.connect(self.PlayButtonClicked)
        self.m_ui.PauseButton.clicked.connect(self.PauseButtonClicked)
        self.m_ui.ResumeButton.clicked.connect(self.ResumeButtonClicked)

    def DisconnectButtonClicked(self):
        self.close()
        mainwindow.close()
        serverwindow.show()
    def BackToPlaylistClicked(self):
        self.close()
        mainwindow.show()
    def StopSongClicked(self):
        global worker
        worker.stop()
        sys
    def PlayButtonClicked(self):

        filename = "serverAddress.txt"
        if os.path.isfile(filename):
            with open(filename, "r") as file:
                serverIP = file.readline().strip("\n")
                serverPort = file.readline()

        SongToPlay = [item.text() for item in self.m_ui.MusicList.selectedItems()]
        SongToPlay = SongToPlay[0].split(" | ")
        
        songID = SongToPlay[0]
        global worker
        worker = Worker(songID, serverIP, serverPort)
        self.threadpool.start(worker)
    def PauseButtonClicked(self):
        global worker
        worker.pause()
    def ResumeButtonClicked(self):
        global worker
        worker.resume()
        

 




def runGUI():
    serverwindow.show()
    #app.exec()

def runMainGUI():
    mainwindow.show()
    #app.exec()

def runServerMenu():
    serverwindow.show()

def runPlaylistMenu():
    playlistwindow.show()

def runMainMenu():
    mainwindow.show()


def runAddMenu():
    addwindow.show()

class Worker(QRunnable):

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.args = args
        self.kwargs = kwargs
        self.is_paused = False
        self.is_stopped = False

    @pyqtSlot()
    def run(self):
        serverIP = self.args[1]
        serverPort = self.args[2]
        songID = self.args[0]
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
            while self.is_paused:
                time.sleep(0)
            if self.is_stopped:
                break

        #cleanup
        stream.stop_stream()
        stream.close()
        pya.terminate()
        s.close()

        
        
    def pause(self):
        self.is_paused = True
    def resume(self):
        self.is_paused = False
    def stop(self):
        self.is_stopped = True


if __name__ == '__main__':
    app = QApplication([])
    serverwindow = ServerMenu()
    mainwindow = MainMenu()
    #playlistwindow = PlaylistMenu()
    addwindow = AddMenu()
    filename = "serverAddress.txt"
    if os.path.isfile(filename):
        with open(filename, "r") as file:
            serverIP = file.readline().strip("\n")
            serverPort = file.readline()
            runMainGUI()

    else:
        
        runGUI()
        with open(filename, "r") as file:
            serverIP = file.readline().strip("\n")
            serverPort = file.readline()
        with open(filename, "w") as file:
            file.write(serverIP+"\n"+serverPort)
    
    sys.exit(app.exec())
    global worker
    app.aboutToQuit.connect(worker.stop)







