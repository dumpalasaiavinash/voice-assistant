from os import listdir
from os.path import isfile, join
from gtts import gTTS
import os
import random
import speech_recognition as sr
import playsound

songs=[f for f in listdir('/Users/ambatianirudh/Desktop/music') if isfile(join('/Users/ambatianirudh/Desktop/music', f))]
print(songs)

def playsong(x):
    if x not in songs:
        print('this song is not available')
    else:
        y='/Users/ambatianirudh/Desktop/music/'+x
        print(y)
        playsound.playsound(y,True)


def playasong():
    a=random.randint(0,3)
    playsong(songs[a])



playasong()

