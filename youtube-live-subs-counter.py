import urllib.request
import json
import time
import os


name = input("Enter the username: ")
timee = int(input("Enter the show time in mins: "))
key = "AIzaSyA_f8mp7MToePDLfxJlB6Lzaozex1owTjU"
timee = timee*60
i = 0
while i <= timee:

    data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername="+name+"&key="+key).read()
    subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
    print(name+" has got "+subs+" right now! ", end='\r')
    time.sleep(1)
    i = i+1
    
