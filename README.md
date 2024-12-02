# SoundAEtherTest1
The repository for our project code.

First of all there are a few things to note about this application. There are two branches, the main branch uses a gui for the client and the terminal for the server, and the rewrite branch is all in the terminal. Choose which ever one you prefer and download all of the files and put them into a folder. You will need to have python installed, as well as PyQt6 for the GUI version, among other python libraries. The ones that you need can be found at the top of each of the files. Make sure that when you install them that the libraries are able to be accessed by the files, otherwse nothing will work. Once everyhting is set up correctly, to get it to work properly first run the file "server.py" on the computer you wish to host the music. You will then have to opportunity to add songs, add playlists, edit playlists, remove songs and playlists, view what is currently in the database, and start up the server. You must add the songs you want to listen to before you start up the server. Please note that at the moment the application only accepts .wav files, so please make sure that that is what you are uploading. If anything happens that corrupts or messes with the database, you may have to delete the file labeled "database" in the folder and then run "server.py" to make a new one and add songs to that. Once you are ready to use the client, start up the server and take note of what port it says it is listening to. When you run the client, either the terminal or the gui version, you will need to type in the port number, as well as the ipv4 ip address of the server you are trying to connect to. If you are using local host you can type in "-1" for the ip address. If you make a mistake or something happens that makes connecting to the server impossible, you may have to delete the file labelled "serverAddress" and start over from the beginning. Otherwise, the client should remember the ip and port number so you will not have to log in multiple times. Everything should work in the terminal version, but in the GUI version there are a few things that you should take note of. Firstly, the "Add Songs" menu is at the moment non-functional. You can get to the menu but you cannot add songs from the client side at the moment. Also the "Add playlist" button is non-functional. Both of these activites must be completed on the server side only. Otherwise, on the main menu you are free to select which playlist you want and press the "select" button to go to the playlist menu, where you can listen to songs. In the playlist menu you can select a song and start listening to it by pressing the play button. Once the song has started, you can pause it by pressing pause, and then press resume to resume, or you can press "Stop". PLEASE NOTE that pressing STOP will disconnect you from the server and cause the server to shut down. You will need to start up the server again if you press "Stop" while a song is playing. Also the disconnect button may not work correctly. If you wish to disconnect or connect to another server, please delete the "serverAddress" file and enter in the information again. 

ALSO IMPORTANT NOTE: If you choose to download the GUI version, you will need all of the other files on the main branch. The branch files will not work! Please keep this in mind!
