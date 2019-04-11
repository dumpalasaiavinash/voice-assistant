import speech_recognition as sr
from gtts import gTTS
import os
import requests
import webbrowser



"""out=gTTS(text="what is ur name",lang='en-us')
out.save("hang.mp3")
os.system("mpg321 hang.mp3")

name = input("What is your name? ")



out=gTTS(text="hello "+name,lang='en-us')
out.save("hang.mp3")
os.system("mpg321 hang.mp3")"""
turns = 10
#print("Time to play hangman!")
out=gTTS(text="lets play hangman",lang='en-us')
out.save("hang.mp3")
os.system("mpg321 hang.mp3")

print("You have", + turns, 'more guesses')
cf = "you have" + str(turns) + "more guesses"
out = gTTS(text=cf, lang='en-us')
out.save("hang.mp3")
os.system("mpg321 hang.mp3")

print("Start guessing...")
"""out=gTTS(text="Start guessing",lang='en-us')
out.save("hang.mp3")
os.system("mpg321 hang.mp3")"""
word = "prosthetics"

guesses = ''



while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char,end="")
            """out = gTTS(text=char, lang='en-us')
            out.save("hang.mp3")
            os.system("mpg321 hang.mp3")"""
        else:
            print("_",end="")
            """out = gTTS(text="_", lang='en-us')
            out.save("hang.mp3")
            os.system("mpg321 hang.mp3")"""
            failed += 1
    if failed == 0:
        print("You won")
        out = gTTS(text="You won.       ,The word is "+word, lang='en-us')
        out.save("hang.mp3")
        os.system("mpg321 hang.mp3")
        break
    out = gTTS(text="guess a character", lang='en-us')
    out.save("hang.mp3")
    os.system("mpg321 hang.mp3")
    #guess = input("\nguess a character:")
    r = sr.Recognizer()
    with sr.Microphone() as source:
      print("Say something!")
      audio = r.listen(source)
      res=r.recognize_google(audio)
      print("You said: " + res)
    guess=res
    guesses += guess

    if guess in word:
       print("yes "+guess+" is present in the word")
       jk="yes "+guess+" is present in the word"
       out = gTTS(text=jk, lang='en-us')
       out.save("hang.mp3")
       os.system("mpg321 hang.mp3")

    if guess not in word:
      turns -= 1
      print("Wrong")
      out = gTTS(text="wrong", lang='en-us')
      out.save("hang.mp3")
      os.system("mpg321 hang.mp3")
      print("You have", + turns, 'more guesses')
      cf="you have"+str(turns)+"more guesses"
      out = gTTS(text=cf, lang='en-us')
      out.save("hang.mp3")
      os.system("mpg321 hang.mp3")
    if turns == 0:
      print("You Loose")
      out = gTTS(text="you loose", lang='en-us')
      out.save("hang.mp3")
      os.system("mpg321 hang.mp3")
