# Musicterm
A python program to listen to music in terminal.

## Dependencies
They are some python3 libraries: **pytube**, **pyfiglet**, **youtube-search-python** and **colorama**.                                                 
Also you need **ffplay** command from **FFmpeg**.

## How it works
This scripts just downloads audio from youtube videos, no api or anything like that needed.                 
Then when is requested it executes the **ffplay** command and starts the music.                                

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
8 : rmfp - To REMOVE a song out of a playlist        
9 : psong - To REPRODUCE a songe alone       
10: dplaylists - To DISPLAY all the playlists       
11: dasongs - To DISPLAY all the downloaded songs        
12: exit - To EXIT the program          
       
All this is in manual.txt :)      

## Installing
Ffplay is needed, install it depending of your operating system.          
Except that you can run this code to install the other dependencies.
```
git clone https://github.com/Kik449/musicterm
cd musicterm
bash install_py.sh
python3 musicterm.py
```
## Info
Developed and tested in **Linux Lite** with NVIM editor.
