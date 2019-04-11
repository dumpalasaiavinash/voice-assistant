import requests
from gtts import gTTS
import os

tabUrl="https://www.flipkart.com/search?q=";
term=input("enter u r search: ")

link=tabUrl + term
f = requests.get(link)
new=2
a=f.text
b=a.find("1vC4OE _2rQ-NK")
c=a.find("_3wU53n")
if b==-1:
    b=a.find('1vC4OE"')
    c=a.find("_2cLu-l" )
    name=""
    for i in range(16,100):
        if f.text[c+i] == '<' or f.text[c+i] == '>' or f.text[c+i] == '"':
            break
        name = name + f.text[c + i]
    price=""
    for i in range(96,120):
        if f.text[b+i] == '<' or f.text[b+i] == '>' or f.text[b+i] == '"':
            break
        price=price + f.text[b+i]
    if price=='refetch':
        output="NO RESULTS FOUND FOR YOUR QUERY"
        print(output)
        tts = gTTS(text=output, lang='en-us')
        tts.save("hel.mp3")
        os.system("mpg321 hel.mp3")
    else:
        output = name + " costs " + price+" rupees"
        print(output)
        tts = gTTS(text=output, lang='en-us')
        tts.save("hel.mp3")
        os.system("mpg321 hel.mp3")
else:
    name=""
    for i in range(28,130):
        if f.text[c+i] == '<' or f.text[c+i] == '>' or f.text[c+i] == '"':
            break
        name=name + f.text[c+i]
    price=""
    for i in range(104,120):
        if f.text[b+i] == '<' or f.text[b+i] == '>' or f.text[b+i] == '"':
            break
        price=price + f.text[b+i]
    output=name + " costs " + price+" rupees"
    print(output)

    tts = gTTS(text=output, lang='en-us')
    tts.save("hel.mp3")
    os.system("mpg321 hel.mp3")
