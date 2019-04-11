import requests
import webbrowser
import speech_recognition as sr
from gtts import gTTS
import os





#a = input("train no : ")
#a=a.lower()



def trainno():
    tts = gTTS(text="tell your train number or train name", lang='en-us')
    tts.save("hel.mp3")
    os.system("mpg321 hel.mp3")

    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    a = r.recognize_google(audio)
    a = a.lower()
    print("You said: " + a)

    a=a.replace("coromandal express","12841")
    a=a.replace("godavari express","12727")
    a=a.replace("charminar express","12759")
    a=a.replace("chennai express","12604")
    a=a.replace("tungabhadra express","17024")
    a=a.replace("duronto express","12285")
    a=a.replace("rajdhani express","12437")
    a=a.replace("hyderabad express","12603")
    a=a.replace("bangalore express ","06514")
    a=a.replace("falknuma express","12703")
    a=a.replace("konark express","11020")
    a=a.replace("prasanthi express","18464")
    a=a.replace("circar express","17643")
    a=a.replace("visakha express","17015")



    link="https://erail.in/train-running-status/" + a
    new=2
    #webbrowser.open(link,new=new)



    f = requests.get(link)

    #print(f.text)
    c=f.text
    d=c.find("description")
    #print(d)
    train=""
    for i in range(d + 22 , 10000):
        if  f.text[i] == '.' or f.text[i]=='/':
           break
        train = train + f.text[i]
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
