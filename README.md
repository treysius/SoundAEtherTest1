# SoundAEtherTest1
The repository for our project code.

First things first, you need to put all of the files into a folder, and call it whatever you want. I called it PythonTestServer.

You will need FFmpeg to be installed on your computer, and ideally have the folder in the same folder as all the other project stuff.

Make sure you have Pyaudio, pickle, struct, keyboard, and mutagen pip installed and accessable by the python files.

Make sure that "host_ip" in both the client and server are set to your ip address. "127.0.0.1" will not work it has to be your ip address.

In MetadataTest1 you need to change the string in "os.fencode" to be the path to the directory you have made for this project.

Also in Metadata1, you will need to change the string "command" to have the correct path to your directory.

In Test1Server there are two occurences of "command" that also need to be changed.

To add music, simply drag the file into the directory with all of the other files, then run "MetadataTest1".

To play music, you should first run Test1Server and follow the instructions in the terminal, then run ClientTest1 on the client machine and the song you selected
on the server will play.

This is not complete at all, but does mostly work.
