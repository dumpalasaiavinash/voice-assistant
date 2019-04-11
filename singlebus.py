from gtts import gTTS
import os
import speech_recognition as sr
import random

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

def busbuzz():
 l=['bus','buzz','bus buzz']
 c=1

 while(c>0):
     if(c%2!=0 and c%3==0 and c%5!=0):
      print("bus")
      talk("bus")
     elif(c%2!=0 and c%3!=0 and c%5==0):
      print("buzz")
      talk("buzz")
     elif (c % 2 != 0 and c%3== 0 and c % 5 == 0):
      print("bus buzz")
      talk("bus buzz")
     else:
      print(c)
      talk(str(c))
     c=c+1
     if (c % 2 == 0 and c % 3 == 0 and c % 5 != 0):
      b = recognize()
      if(b=='to'):
       b=2
      if(b!=l[0]):
       print("you lost")
       talk("you lost")
       break
     elif (c % 2 == 0 and c % 3 != 0 and c % 5 == 0):
      b = recognize()
      if(b=='to'):
       b=2

      if (b != l[1]):
       print("you lost")
       talk("you lost")
       break
     elif (c % 2 == 0 and c % 3 == 0 and c % 5 == 0):
      b = recognize()
      if(b=='to'):
       b=2
      #b=str(input(" "))
      if (b != l[2]):
       print("you lost")
       talk("you lost")
       break
     else:
      b = recognize()
      if(b=='to'):
       b=2
      #b=eval(input(" "))
      if(c%2==0 and b!=c):
       print("you lost the game")
       talk("you lost")
       break
     c=c+1

