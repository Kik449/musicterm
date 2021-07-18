# Musicterm
A python program to listen to music in terminal.

## Dependencies
They are some python3 libraries: **pytube**, **pyfiglet**, **youtube-search-python** and **colorama**.                                                 
Also you need **ffplay** command from **FFmeg**.

## How it works
This scripts just downloads audio from youtube videos, no api or anything like that needed.                 
Then when is requested it executes the **ffplay** command and starts the music.                                

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
