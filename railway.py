import requests
import webbrowser
import speech_recognition as sr
from gtts import gTTS
import os


def stations():
    tts = gTTS(text="from", lang='en-us')
    tts.save("hel.mp3")
    os.system("mpg321 hel.mp3")

    print("enter your starting and ending point")
    #a = input("FROM : ")
    #b = input("TO : ")

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("from")
        audio = r.listen(source)
    a=r.recognize_google(audio)
    a=a.lower()
    print("You said: " + a)

    tts = gTTS(text="To", lang='en-us')
    tts.save("hel.mp3")
    os.system("mpg321 hel.mp3")

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("to")
        audio = r.listen(source)
    b=r.recognize_google(audio)
    b=b.lower()
    print("You said: " + b)

    a=a.replace("bengaluru","ksr-bengaluru-SBC")
    a=a.replace("chennai","chennai-central-MAS")
    a=a.replace("secunderabad" or "sc","secunderabad-jn-SC")
    a=a.replace("delhi","delhi-DLI")
    a=a.replace("hyderabad" or "hyd","secunderabad-jn-SC")
    a=a.replace("sullurupeta" or "spe" ,"sullurupeta-SPE")
    a=a.replace("tada","tada-TADA")
    a=a.replace("visakhapatnam"or"vskp","visakhapatnam-VSKP")
    a=a.replace("vijayawada" or "bza","vijayawada-jn-BZA")
    a=a.replace("mumbai","mumbai-central-BCT")


    b=b.replace("bengaluru","ksr-bengaluru-SBC")
    b=b.replace("chennai","chennai-central-MAS")
    b=b.replace("secunderabad" or "sc","secunderabad-jn-SC")
    b=b.replace("delhi","delhi-DLI")
    b=b.replace("hyderabad" or "hyd","secunderabad-jn-SC")
    b=b.replace("sullurupeta" or "spe","sullurupeta-SPE")
    b=b.replace("tada","tada-TADA")
    b=b.replace("visakhapatnam"or"vskp","visakhapatnam-VSKP")
    b=b.replace("vijayawada" or "bza","vijayawada-jn-BZA")
    b=b.replace("mumbai","mumbai-central-BCT")


    link="https://erail.in/trains-between-stations/" + a + "/" + b
    new=2
    #webbrowser.open(link,new=new)



    f = requests.get(link)

#    print(f.text)
    c=f.text
    d=c.find("<title>")
    #print(d)
    train=""
    for i in range(d+8,1000):
        if  f.text[i] == '-':
            break
        train=train + f.text[i]
    print(train)


    tts = gTTS(text=train, lang='en-us')
    tts.save("hel.mp3")
    os.system("mpg321 hel.mp3")


    # bengaluru = ksr-bengaluru-SBC
    # chennai = chennai-central-MAS
    # secunderabad-jn-SC/delhi-DLI
    # sullurupeta-SPE/tada-TADA
    #visakhapatnam-VSKP/vijayawada-jn-BZA
    #https://erail.in/train-running-status/12727
stations()