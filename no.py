import random
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

def numbergame():
 a=random.randint(222,999)
 print(a)
 talk(str(a))
 b = recognize()
 p=0
 c=3

 while(str(a)==str(b)):
  a=a*10+random.randint(1,9)
  print(a)
  talk(str(a))
  b = recognize()
  p+=1
 else:
  talk("You lost")


  
  
  
