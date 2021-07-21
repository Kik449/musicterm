from pytube import YouTube
from youtubesearchpython import VideosSearch
from colorama import Fore
import base64,os,json,pyfiglet

playlists = {}
songs = {}
pla_l = []
son_l = []
alldata = {}
config = {}

def search(content,limit):
    return_dict = {}
    search = VideosSearch(content, limit = limit)
    count = 0
    for video in search.result()["result"]:        
        count += 1
        title = video["title"]
        if len(title) > 40:
            ex = len(title)-37
            title = title[:-ex]+"..."
        if len(title) < 40:
            title += " "*(40-len(title))
        print(config["theme"]["color1"]+str(count)+Fore.RESET+": ("+config["theme"]["color2"]+title+Fore.RESET+")---("+config["theme"]["color3"]+video["duration"]+Fore.RESET+")")
        return_dict[count-1] = { "title": content.replace(" ","_"),"url":video["link"],"time": video["duration"]}
    option = input(config["theme"]["color4"]+"Select a song"+Fore.RESET+"~$ ")
    return return_dict[int(option)-1]

def base64_encoding(text):
    text_bytes = text.encode('utf-8')
    base64_bytes = base64.b64encode(text_bytes)
    base64_text = base64_bytes.decode('utf-8')
    return base64_text

def base64_decoding(base64_text):
    base64_bytes = base64_text.encode('utf-8')
    text_bytes = base64.b64decode(base64_bytes)
    text_bytes = (str(text_bytes).replace("\xa7","")).encode('utf-8')
    text = text_bytes.decode('utf-8')
    return text

def download_mp3(url,title):
    yt_video = YouTube(url)
    audio = yt_video.streams.filter(only_audio=True).first()
    out_file = audio.download(output_path="musicterm",filename=base64_encoding(title))

def add_to_playlist(song,playlist):
    playlists[playlist]["songs"].append(song)

def play_song(title):
    os.system("ffplay -autoexit -loglevel quiet -volume " + str(config["volume"])+" -nodisp "+title+".mp4 > /dev/null" )

def create_playlist(name):
    playlists[name] = {}
    playlists[name]["songs"] = []
    playlists[name]["name"] = name
    pla_l.append(playlists[name])

def display_playlists():
    count = 0
    for playlist in pla_l:
        count += 1
        print(config["theme"]["color1"]+str(count)+Fore.RESET+": ("+config["theme"]["color2"]+playlist["name"]+Fore.RESET+")---("+config["theme"]["color3"]+str(len(playlist["songs"]))+Fore.RESET+")")

def play_playlist(playlist):
    for song in playlists[playlist]["songs"]:
        print("\b\b"+config["theme"]["color1"]+"Playing: "+config["theme"]["color5"]+ song["title"]+config["theme"]["color4"]+" ^C "+config["theme"]["color3"]+">>"+Fore.RESET)
        play_song("musicterm/"+base64_encoding(song["title"]))

def display_songs(playlist):
    count = 0
    for song in playlists[playlist]["songs"]:
        count += 1
        print(config["theme"]["color1"]+str(count)+Fore.RESET+": ("+config["theme"]["color2"]+song["title"]+Fore.RESET+")---("+config["theme"]["color2"]+song["time"]+Fore.RESET+")")

def delete_playlist(playlist):
    del playlists[playlist]
    count = 0
    for playlist in pla_l:
        count += 1
        if playlist["name"] == playlist:
            del pla_l[count-1]
def delete_song(song):                                                                        
    del songs[song["title"]]
    count = 0
    for s in son_l:
        count += 1
        if s["title"] == song["title"]:
            del son_l[count-1]


def delete_from_playlist(playlist,song):
    count = 0
    for s in playlists[playlist]["songs"]:
        count += 1
        if s["title"] == song["title"]:
            del playlists[playlist]["songs"][count-1]

def save_json(dicti,name):
    file = open(name,"wt")
    file.write(json.dumps(dicti))
    file.close()

def load_json(name):
    file = open(name,"rb")
    content = file.read()
    file.close()
    return json.loads(content)

def display_all_songs():
    count = 0
    for song in son_l:
        count += 1
        print(Fore.LIGHTRED_EX+str(count)+Fore.RESET+": ("+Fore.BLUE+song["title"]+Fore.RESET+")---("+Fore.GREEN+song["time"]+Fore.RESET+")")       

try:
    config = load_json("config.json")
    alldata = load_json("data.json")
    playlists = alldata["playlists"]
    songs = alldata["songs"]
    son_l = alldata["son_l"]
    pla_l = alldata["pla_l"]
    exit = False
except:
    print("No data or config file founed!")
banner = pyfiglet.figlet_format(config["banner_text"], font = "slant"  )
print(config["theme"]["color3"] + banner + Fore.RESET)
while(not exit):
    try:
        y = input(config["theme"]["color1"]+"\b\bTERM"+Fore.RESET+"~$ ")
        y_s = y.split(" ")
        if y_s[0] == "download":
            song = search(input(config["theme"]["color4"]+"Song Name"+Fore.RESET+"~$ "),9)
            if song["title"] in songs:
                raise Exception("")
            download_mp3(song["url"],song["title"])
            songs[song["title"]] = song
            son_l.append(song)
            print(config["theme"]["color2"]+song["title"]+Fore.RESET+" downloaded!")
        if y_s[0] == "mkplaylist":
            pname = input(config["theme"]["color4"]+"Playlist Name"+Fore.RESET+"~$ ")
            create_playlist(pname)
        if y_s[0] == "rmplaylist":
            pname = input(config["theme"]["color4"]+"Playlist Name"+Fore.RESET+"~$ ")
            delete_playlist(pname)
        if y_s[0] == "rmsong":
            sname = input(config["theme"]["color4"]+"Song Name"+Fore.RESET+"~$ ")
            delete_song(songs[sname])
        if y_s[0] == "append":
            pname = input(config["theme"]["color4"]+"Playlist Name"+Fore.RESET+"~$ ")
            sname = input(config["theme"]["color4"]+"Song Name"+Fore.RESET+"~$ ")
            add_to_playlist(songs[sname],pname)
        if y_s[0] == "dsongs":
            pname = input(config["theme"]["color4"]+"Playlist Name"+Fore.RESET+"~$ ")
            display_songs(pname)
        if y_s[0] == "pplaylist":
            pname = input(config["theme"]["color4"]+"Playlist Name"+Fore.RESET+"~$ ")
            play_playlist(pname)
        if y_s[0] == "rmfp":
            pname = input(config["theme"]["color4"]+"Playlist Name"+Fore.RESET+"~$ ")
            sname = input(config["theme"]["color4"]+"Song Name"+Fore.RESET+"~$ ")
            delete_from_playlist(pname,songs[sname])
        if y_s[0] == "psong":
            sname = input(config["theme"]["color4"]+"Song Name"+Fore.RESET+"~$ ")
            print(config["theme"]["color1"]+"\b\bPlaying: "+config["theme"]["color5"]+ sname+config["theme"]["color4"]+" ^C "+config["theme"]["color3"]+">>"+Fore.RESET)
            play_song("musicterm/"+base64_encoding(songs[sname]["title"]))
        if y_s[0] == "dplaylists":
            display_playlists()
        if y_s[0] == "dasongs":
            display_all_songs()
        if y_s[0] == "exit":
            exit = True
    except Exception as t:
        print("Something "+Fore.LIGHTRED_EX+ "failed" + Fore.RESET + "! ")
print("Bye!")
alldata["playlists"] = playlists
alldata["songs"] = songs
alldata["pla_l"] = pla_l
alldata["son_l"] = son_l
save_json(alldata,"data.json")
