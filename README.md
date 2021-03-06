# Musicterm
A python program to listen to music from INTERNET in terminal.
## WARNING
Musicterm is no longer maintained!
## Image
![musicterm](https://github.com/Kik449/musicterm/raw/main/musicterm.png)
## Update!
Pytube stopped working, I have patched the error.      
Git clone again or if you dont want to loose all the songs and playlists replace the old musicterm.py with the newer one and install youtube_dl library.
## Dependencies
They are some python3 libraries: **youtube_dl**, **youtubesearchpython**, **colorama**, **pyfiglet**.                                              
Also **mpv**, install it with your package manager.
## How it works
This scripts just downloads audio from youtube videos, no api or anything like that needed.                                                 

## Automate tasks with bash
You can automate tasks by making a bash script.    
```bash
{
  echo "command"
} | python3 musicterm.py     
```
For no musicterm output use ```> /dev/null```
```bash
{
  echo "command"
} | python3 musicterm.py > /dev/null
```
Here is an example.
```bash
{
  echo "download" 
  echo "keep ballin"
  echo "1"
  echo "psong"
  echo "keep_ballin"
  echo "exit"
} | python3 musicterm.py     
```
Remember an ```echo "exit"``` allways, otherwise it may crash.
## Usage      
Musicterm works with commands.       
They are 13 commands:         
       
1 : download- To DOWNLOAD the music       
2 : mkplaylist - To CREATE a playlist         
3 : rmplaylist - To REMOVE a playlist        
4 : rmsong - To REMOVE a song        
5 : append - To ADD a song into a playlist        
6 : dsongs - To DISPLAY all the songs in a playlist        
7 : pplaylist - To REPRODUCE an entry playlist        
8 : rmfp - To REMOVE a song from a playlist        
9 : psong - To REPRODUCE a song alone       
10: dplaylists - To DISPLAY all the playlists       
11: dasongs - To DISPLAY all the downloaded songs        
12: exit - To EXIT the program          
13: prplaylist - To REPRODUCE a playlist in a random order              
       
All this is in manual.txt :)      
## Configuration        
In the config file you can change the banner text in banner_text and colors.
### Colors cheatsheet
Prefix: ```\u001b[```
#### Normal&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Light
BLACK 30m&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;BLACK 90m   
RED 31m&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;RED 91m    
GREEN 32m&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; GREEN 92m      
YELLOW 33m&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;YELLOW 93m      
BLUE 34m&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;BLUE 94m            
CYAN 36m&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CYAN 96m      
WHITE 37m&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;WHITE 97m     
## Installing
Since ffplay was removed, now it uses playsound library.
To install all the libraries
```
pip3 install pyfiglet
pip3 install youtube-search-python
pip3 install youtube-dl
pip3 install colorama
```
## Info
Developed and tested in **Linux Lite**, **Kali Linux** and **Arch** with NVIM editor.      
And some features in Pops with the help of [ru55o](https://github.com/byru55o).
