from youtube_dl import YoutubeDL
from youtubesearchpython import VideosSearch
from colorama import Fore
from multiprocessing import Process
from pyfiglet import figlet_format 
import base64,json,random,os

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
    try:
        for video in search.result()["result"]:        
            count += 1
            title = video["title"]
            if len(title) > 40:
                ex = len(title)-37
                title = title[:-ex]+"..."
            if len(title) < 40:
                title += " "*(40-len(title))
            print(config["theme"]["color1"]+str(count)+Fore.RESET+": ("+config["theme"]["color2"]+str(title)+Fore.RESET+")---("+config["theme"]["color3"]+str(video["duration"])+Fore.RESET+")")
            return_dict[count-1] = { "title": content.replace(" ","_"),"url":video["link"],"time": video["duration"]}
    except:
        pass
    if len(return_dict) == 0:
        raise Exception("")
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
    song_downloader = YoutubeDL({'no-warnings':True,'quiet':True,'format':'bestaudio','outtmpl':'musicterm/'+base64_encoding(title)+'.mp3'})
    song_downloader.extract_info(url)

def add_to_playlist(song,playlist):
    playlists[playlist]["songs"].append(song)

def play_song(title):
    print("\b"*30+config["theme"]["color1"]+"\b\bPlaying: "+config["theme"]["color5"]+ title+config["theme"]["color4"]+" ^C "+config["theme"]["color3"]+">>"+Fore.RESET)
    try:
        os.system("mpv musicterm/"+base64_encoding(title)+".mp3")
    except:
        pass

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

def random_playlist(pname):
    ps = playlists[pname]["songs"]
    max_len = len(ps)
    rv = []
    generated = False
    for i in range(0 , max_len):
        rv.append(i)
    random.shuffle(rv)
    for i in rv:
        sname = ps[rv[i]]["title"]
        play_song(sname)

def play_playlist(playlist):
    for song in playlists[playlist]["songs"]:
        play_song(song["title"])

def display_songs(playlist):
    count = 0
    for song in playlists[playlist]["songs"]:
        count += 1
        print(config["theme"]["color1"]+str(count)+Fore.RESET+": ("+config["theme"]["color2"]+song["title"]+Fore.RESET+")---("+config["theme"]["color3"]+song["time"]+Fore.RESET+")")

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

def save_json(jdict,name):
    file = open(name,"wt")
    file.write(json.dumps(jdict))
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
        print(config["theme"]["color1"]+str(count)+Fore.RESET+": ("+config["theme"]["color2"]+song["title"]+Fore.RESET+")---("+config["theme"]["color3"]+song["time"]+Fore.RESET+")")

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
banner = figlet_format(config["banner_text"], font = "slant")
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
        if y_s[0] == "prplaylist":
            pname = input(config["theme"]["color4"]+"Playlist Name"+Fore.RESET+"~$ ")
            random_playlist(pname)
        if y_s[0] == "rmfp":
            pname = input(config["theme"]["color4"]+"Playlist Name"+Fore.RESET+"~$ ")
            sname = input(config["theme"]["color4"]+"Song Name"+Fore.RESET+"~$ ")
            delete_from_playlist(pname,songs[sname])
        if y_s[0] == "psong":
            sname = input(config["theme"]["color4"]+"Song Name"+Fore.RESET+"~$ ")
            play_song(songs[sname]["title"])
        if y_s[0] == "dplaylists":
            display_playlists()
        if y_s[0] == "dasongs":
            display_all_songs()
        if y_s[0] == "exit":
            exit = True
        alldata["playlists"] = playlists
        alldata["songs"] = songs
        alldata["pla_l"] = pla_l
        alldata["son_l"] = son_l
        save_json(alldata,"data.json")
    except Exception as e:
        print("Something "+Fore.LIGHTRED_EX+ "failed" + Fore.RESET + "!")
print("Bye!")
alldata["playlists"] = playlists
alldata["songs"] = songs
alldata["pla_l"] = pla_l
alldata["son_l"] = son_l
save_json(alldata,"data.json")
