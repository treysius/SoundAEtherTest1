import mutagen
import os
import sqlite3

#import mutagen.id3

directory = os.fsencode(r"C:\Users\treys\PythonTestServer")
FileNameList =[]
TitleList = []
ArtistList1 = []
ArtistList2 = []
SongLengthList = []


for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if (filename.endswith(".mp3") and filename!="MetaTemp.mp3") or filename.endswith(".m4a"):
        os.rename(filename, "_".join(filename.split()))
        filename = "_".join(filename.split())
        print(filename)
        command = "cd\\ && cd Users\\treys\\PythonTestServer && ffmpeg -i {} -ab 160k -ac 2 -ar 44100 -vn {} -y".format(filename,'MetaTemp.mp3')
        os.system(command)

        MetadataDict = mutagen.File("MetaTemp.mp3")
        FileNameList.append(filename)
        TitleList.append(str(MetadataDict.get('TIT2')))
        ArtistList1.append(str(MetadataDict.get('TPE1')))
        ArtistList2.append(str(MetadataDict.get('TPE2')))
        SongLengthList.append(round(MetadataDict.info.length))


#filename =  'TestFile7.mp3'
#command = "cd\\ && cd Users\\treys\\PythonTestServer && ffmpeg -i {} -ab 160k -ac 2 -ar 44100 -vn {} -y".format(filename,'MetaTemp.mp3')
#os.system(command)

#command = "mutagen-inspect MetaTemp.mp3"
#os.system(command)

print("--------------------------------------------------------------------------------")

#MetadataDict = mutagen.File("MetaTemp.mp3")

#print(FileNameList)
#print(TitleList) 
#print(ArtistList1) 
#print(ArtistList2)
#print(SongLengthList)

con = sqlite3.connect("SongTest.db")


cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS Playlist1(songindex INT, title VARCHAR(255), artist1 VARCHAR(255), artist2 VARCHAR(255), songlength INT, songfile VARCHAR(255))")

i=0
while i < len(TitleList):
    #tempstr=("INSERT INTO Playlist1 VALUES ('thrax','Caponeti','Novastein', '144', 'TestFile6.mp3')")
    tempstr=(f"""INSERT INTO Playlist1 VALUES ('{i}',"{str(TitleList[i])}","{str(ArtistList1[i])}","{str(ArtistList2[i])}",'{int(SongLengthList[i])}',"{str(FileNameList[i])}")""")
    cur.execute(tempstr)
    i += 1

con.commit()

res = cur.execute("Select * FROM Playlist1")
for row in res:
    print(row)

con.close()

#startsong = int(input("Select the number of the son you wish to listen to..."))

#res = cur.execute(f"Select songfile FROM Playlist1 WHERE songindex={startsong}")

#print("".join(res.fetchone()))