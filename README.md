# Musicterm
A python program to listen to music from INTERNET in terminal.

## Dependencies
They are some python3 libraries: **youtube_dl**, **pyfiglet**, **youtube-search-python** and **colorama**.                                                 
Also you need **ffplay** command from **FFmpeg**.

## How it works
This scripts just downloads audio from youtube videos, no api or anything like that needed.                 
Then when is requested it executes the **ffplay** command and starts the music.                                

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
They are 12 commands:         
       
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
       
All this is in manual.txt :)      
## Configuration        
Set the volume from 0-100 in string format not int (save the value from 0-100 between ```"```)           
In the config file you can also change the banner text in banner_text.
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
Ffplay is needed, install it depending of your operating system or linux ditro. 
```
apt: sudo apt install ffmpeg
snap: sudo snap install ffmpeg
```
Run this code where you want to install the program.       
```
git clone https://github.com/Kik449/musicterm
cd musicterm
bash install_py.sh
python3 musicterm.py
```
## Info
Developed and tested in **Linux Lite** with NVIM editor.
