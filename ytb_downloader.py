#!/usr/bin/env python
from pytube import YouTube
import re
import subprocess
from pytube import Playlist
print("""
__  __          __       __         ___                  __             __       
\ \/ /__  __ __/ /___ __/ /  ___   / _ \___ _    _____  / /__  ___ ____/ /__ ____
 \  / _ \/ // / __/ // / _ \/ -_) / // / _ \ |/|/ / _ \/ / _ \/ _ `/ _  / -_) __/
 /_/\___/\_,_/\__/\_,_/_.__/\__/ /____/\___/__,__/_//_/_/\___/\_,_/\_,_/\__/_/   
                                        = Devalfo =
""")
def packer():
    try:
        from pytube import YouTube
        from pytube import Playlist
    except ModuleNotFoundError :
        yn = input("Downloading missing modules[y/n]? :")
        if yn == "y":
            subprocess.call("pip3 install pytube3" , shell = True)
            print("[+]-Done packages are installed")
        elif yn == "n":
            print("ok")
        else :
            print("chose [y/n]")
            print(yn)
packer()
link = input("[+]-Paste the youtube link (ex : https://www.youtube.com/watch?v=W9nZ6u15yis) : ")
def LinkChecker():
    if "https://www.youtube.com/watch?v=" in link :
        print("[+]-This link is available")
    else:
        print("[+]-This link is unavailable")
LinkChecker()
url = YouTube(link)
strs=url.streams
it = 0
def downloader():

    for lin in strs:
        global it
        it = int ( it ) + 1
        #print(i , "-" ,  lin)
        typ = re.findall("/\w\w\w",str(lin))
        gr = re.findall("(?:res=)(.*fps)" , str(lin))
        if typ:
            for tp in typ:
                for g in gr:
                    print("[",it,"]-" , "Type :" , tp  , "," "Resolution :", g)
        else:
            print("[+]-Error this link isn't available")
    tf = int(input("[+]-Chose a video type : "))
    if it<tf :
        print("[+]-This number isn't in the list try again")
        downloader()
    tf = tf - 1
    try :
        url.streams[tf].download()
        print("[+]-The video is succesfully downloaded")
    except PermissionError :
        print("[+]-Error:Run program as root")
        quit()

downloader()