import pymysql
from gtts import gTTS
import os
import speech_recognition as sr
import random
import pyaudio

def recognize():
 try:
  r = sr.Recognizer()
  with sr.Microphone() as source:
   print("Say something!")
   audio=r.listen(source)
   output = r.recognize_google(audio)
   print(output)
   return output
 except:
  output=''
  return output



def talk(u):
 tts = gTTS(text=u, lang='en-us')
 tts.save("hel.mp3")
 os.system("mpg321 hel.mp3")

def rockpaperscissors():
    temp=0
    s1=0
    s2=0
    while(temp==0):
        a = random.randint(0, 2)
        l = ['rock', 'paper', 'scissor']
        p1 = 0
        p2 = 0
        talk("What do you choose")
        k = recognize()
        print(k)
        if(k=='hey buddy stop'):
            s1=str(s1)
            talk("Here are the scores ")
            talk("I got")
            talk(s1)
            s2=str(s2)
            talk("You scored")
            talk(s2)
            break
        if (a == 0):
            print("a choosed rock..")
            talk("rock")
            if (l[0] == k):
                print("b choosed rock")
                p1 = 0
                p2 = 0
            elif (l[1] == k):
                print("b choosed paper")
                p1 = 0
                p2 = 1
            elif (l[2] == k):
                print("b choosed scissors..")
                p1 = 1
                p2 = 0

        elif(a == 1):
            print("a choosed paper..")
            talk("paper")
            if (l[0] ==k):
                print("b choosed rock")
                p1 = 1
                p2 = 0
            elif (l[1] == k):
                print("b choosed paper")
                p1 = 0
                p2 = 0
            elif (l[2] == k):
                print("b choosed scissors..")
                p1 = 0
                p2 = 1

        elif (a == 2):
            print("a choosed scissors..")
            talk("scissors")
            if (l[0] == k):
                print("b choosed rock")
                p1 = 0
                p2 = 1
            elif (l[1] ==k):
                print("b choosed paper")
                p1 = 1
                p2 = 0
            elif (l[2] == k):
                print("b choosed scissors..")
                p1 = 0
                p2 = 0

        if (p1 > p2):
         print("player a won..")
         talk("i won the game")
         s1+=1
        elif (p1 == p2):
         print("draw..")
         talk("draw")
         s2+=1
        else:
         print("player b won")
         talk("you won , congratulations")

