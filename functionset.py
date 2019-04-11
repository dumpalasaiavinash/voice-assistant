import requests
import re
from gtts import gTTS
import os
from datetime import datetime
from time import gmtime,strftime
import webbrowser
from os import listdir
from os.path import isfile, join
import random
import speech_recognition as sr

riddles=['what can you never eat during the lunch or supper','give me food and i will live give me water and i will die.what am I','what is full of holes but can still hold water','everyone is attracted to me and everybody falls for me.what am I','what gets wetter the longer it is left out in the sun' ]


def sayout(inp):
    tts = gTTS(text=inp, lang='en-us')
    tts.save("hel.mp3")
    os.system("mpg321 hel.mp3")

def genkeyw(text):
    keygen={'buddy','hey', 'who', 'where', 'with', "what's", 'of', 'for', 'at', 'want', 'to', 'me', 'can', 'what', 'when', 'why', 'is', 'am', 'on', 'it', 'if', 'a', 'an', 'the', 'in','are', 'were', 'now', 'my','how', 'you', 'your', 'i'}
    text=text.split()
    s=set(text)
    s=s-keygen
    print(s)
    return s

def ask_a_riddle():
    a=random.randint(0,4)
    tts = gTTS(text=riddles[a],lang='en-us')
    tts.save("hel.mp3")
    os.system("mpg321 hel.mp3")
    print(riddles[a])

    ans = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = ans.listen(source)
    print("You said: " + ans.recognize_google(audio))
    answer = ans.recognize_google(audio)
    if(a==0):
        if(answer=='breakfast'):
            print('correct,you won')
            opt='correct,you won'
            tts = gTTS(text='correct,you won', lang='en-us')
            tts.save("hel.mp3")
            os.system("mpg321 hel.mp3")
            return opt
        else:
            print('sorry,you lost')
            opt='sorry,you lost the answer is breakfast'
            tts = gTTS(text='sorry,you lost the answer is breakfast', lang='en-us')
            tts.save("hel.mp3")
            os.system("mpg321 hel.mp3")
            return opt
    if (a == 1):
        if (answer == 'fire'):
            print('correct,you won')
            opt = 'correct,you won'
            tts = gTTS(text='correct,you won', lang='en-us')
            tts.save("hel.mp3")
            os.system("mpg321 hel.mp3")
            return opt
        else:
            print('sorry,you lost')
            opt='sorry,you lost,the answer is fire'
            tts = gTTS(text='sorry,you lost,the answer is fire', lang='en-us')
            tts.save("hel.mp3")
            os.system("mpg321 hel.mp3")
            return opt
    if (a == 2):
        if (answer == 'sponge'):
            print('correct,you won')
            opt='correct,you won'
            tts = gTTS(text='correct,you won', lang='en-us')
            tts.save("hel.mp3")
            os.system("mpg321 hel.mp3")
            return opt
        else:
            print('sorry,you lost')
            tts = gTTS(text='sorry,you lost,the answer is sponge', lang='en-us')
            opt='sorry,you lost,the answer is sponge'
            tts.save("hel.mp3")
            os.system("mpg321 hel.mp3")
            return opt
    if (a == 3):
        if (answer == 'Gravity'):
            print('correct,you won')
            opt='correct,you won'
            tts = gTTS(text='correct,you won', lang='en-us')
            tts.save("hel.mp3")
            os.system("mpg321 hel.mp3")
            return opt
        else:
            print('sorry,you lost')
            opt='sorry,you lost,the answer is gravity'
            tts = gTTS(text='sorry,you lost,the answer is gravity', lang='en-us')
            tts.save("hel.mp3")
            os.system("mpg321 hel.mp3")
            return opt
    if (a == 4):
        if (answer == 'ice'):
            print('correct,you won')
            opt='correct,you won'
            tts = gTTS(text='correct,you won', lang='en-us')
            tts.save("hel.mp3")
            os.system("mpg321 hel.mp3")
            return opt
        else:
            print('sorry,you lost')
            opt='sorry,you lost,the answer is ice'
            tts = gTTS(text='sorry,you lost,the answer is ice', lang='en-us')
            tts.save("hel.mp3")
            os.system("mpg321 hel.mp3")
            return opt



def time():
    s = strftime('%H%M')
    re=datetime.strptime(s,'%H%M').strftime('%I:%M%p')
    tts = gTTS(text=re, lang='en-us')
    tts.save("hel.mp3")
    os.system("mpg321 hel.mp3")
    return re

def date():
    re=strftime('%d')
    ra=strftime('%B')
    tts = gTTS(text=re+'th'+ra, lang='en-us')
    tts.save("hel.mp3")
    os.system("mpg321 hel.mp3")
    return re

def day():
    re=strftime('%A')
    tts = gTTS(text=re, lang='en-us')
    tts.save("hel.mp3")
    os.system("mpg321 hel.mp3")
    return re

def playrandom():
    songs = [f for f in listdir('/Users/ambatianirudh/Desktop/music') if isfile(join('/Users/ambatianirudh/Desktop/music', f))]
    print(songs)
    a = random.randint(0, 12)
    path='/Users/ambatianirudh/Desktop/music/'+ str(songs[a])
    os.system("mpg321 "+path)

def googleit(res):
    link = "https://www.google.co.in/search?q=" + res
    new = 2
    webbrowser.open(link, new=new)

def sayweather(address):
    api_key = "AIzaSyC-PM-difZHAVazccuVY0jymsI-sgvugqg"
    api_response = requests.get(
        'https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}'.format(address, api_key))
    api_response_dict = api_response.json()

    if api_response_dict['status'] == 'OK':
        latitude = api_response_dict['results'][0]['geometry']['location']['lat']
        longitude = api_response_dict['results'][0]['geometry']['location']['lng']
        print('Latitude:', latitude)
        print('Longitude:', longitude)

    lat = str(latitude) + ',' + str(longitude)
    print(lat)
    lin = "https://weather.com/en-IN/weather/today/l/"
    link = lin + lat
    f = requests.get(link)
    # print(f.text)
    a = f.text
    b = a.find('<span class="styles-xz0ANuUJ__temperature__3Ph8k">')
    # print(b)
    temp = ""
    for i in range(50, 53):
        if f.text[b + i] == '<':
            break
        temp = temp + f.text[b + i]

    output = "the temperature at " + address + " is " + temp + " degree centigrade"
    print(temp + " degree centigrade")

    tts = gTTS(text=output, lang='en-us')
    tts.save("hel.mp3")
    os.system("mpg321 hel.mp3")
    return output


def add_to_shopping_list(item):
    fp = open('a.txt', 'a')
    fp.write(item + '\n')
    fp.close()

def read_shopping_list():
    fp = open('a.txt', 'r')
    data = fp.readlines()
    x=''
    for line in data:
        if line=='set()':
            continue
        x = x + line
    fp.close()
    tts = gTTS(text=x, lang='en-us')
    tts.save("hel.mp3")
    os.system("mpg321 hel.mp3")
    return x


def delete_shopping_list():
    fp = open('a.txt', 'r+')
    fp.truncate()
    fp.close()


def delete_from_shopping_list(item):
    fp = open("a.txt", "r")
    d = fp.readlines()
    fp.close()
    fp = open("a.txt", "w")
    for line in d:
        if item not in line:
            fp.write(line)
    fp.close()


def new_shopping_list():
    tts = gTTS(text="the previous contents gets deleted,say yes to continue", lang='en-us')
    tts.save("hel.mp3")
    os.system("mpg321 hel.mp3")
    choice1 = sr.Recognizer()
    with sr.Microphone() as source:
        audio = choice1.listen(source)
    print("You said: " + choice1.recognize_google(audio))
    if (choice1.recognize_google(audio) == 'yes'):
        delete_shopping_list()




def youtube(res):
    link = "https://www.youtube.com/results?search_query=" + res
    new = 2
    webbrowser.open(link, new=new)
    f = requests.get(link)


def gettrains(a):
    a = a.replace("coromandal express", "12841")
    a = a.replace("godavari express", "12727")
    a = a.replace("charminar express", "12759")
    a = a.replace("chennai express", "12604")
    a = a.replace("tungabhadra express", "17024")
    a = a.replace("duronto express", "12285")
    a = a.replace("rajdhani express", "12437")
    a = a.replace("hyderabad express", "12603")
    a = a.replace("bangalore express ", "06514")
    a = a.replace("falknuma express", "12703")
    a = a.replace("konark express", "11020")
    a = a.replace("prasanthi express", "18464")
    a = a.replace("circar express", "17643")
    a = a.replace("visakha express", "17015")

    link = "https://erail.in/train-running-status/" + a
    new = 2
    f = requests.get(link)
    c = f.text
    d = c.find("description")
    train = ""
    for i in range(d + 22, 10000):
        if f.text[i] == '.':
            break

        train = train + f.text[i]
    print(train)
    tts = gTTS(text=train, lang='en-us')
    tts.save("hel.mp3")
    os.system("hel.mp3")
    return a


def gettrainsbetween(a,b):
    a = a.replace("bangalore", "ksr-bengaluru-SBC")
    a = a.replace("bengaluru", "ksr-bengaluru-SBC")
    a = a.replace("chennai", "chennai-central-MAS")
    a = a.replace("secunderabad" or "sc", "secunderabad-jn-SC")
    a = a.replace("delhi", "delhi-DLI")
    a = a.replace("hyderabad" or "hyd", "secunderabad-jn-SC")
    a = a.replace("sullurupeta" or "spe", "sullurupeta-SPE")
    a = a.replace("tada", "tada-TADA")
    a = a.replace("visakhapatnam" or "vskp", "visakhapatnam-VSKP")
    a = a.replace("vijayawada" or "bza", "vijayawada-jn-BZA")
    a = a.replace("mumbai", "mumbai-central-BCT")

    b = b.replace("bangalore", "ksr-bengaluru-SBC")
    b = b.replace("bengaluru", "ksr-bengaluru-SBC")
    b = b.replace("chennai", "chennai-central-MAS")
    b = b.replace("secunderabad" or "sc", "secunderabad-jn-SC")
    b = b.replace("delhi", "delhi-DLI")
    b = b.replace("hyderabad" or "hyd", "secunderabad-jn-SC")
    b = b.replace("sullurupeta" or "spe", "sullurupeta-SPE")
    b = b.replace("tada", "tada-TADA")
    b = b.replace("visakhapatnam" or "vskp", "visakhapatnam-VSKP")
    b = b.replace("vijayawada" or "bza", "vijayawada-jn-BZA")
    b = b.replace("mumbai", "mumbai-central-BCT")

    link = "https://erail.in/trains-between-stations/" + a + "/" + b
    new = 2

    f = requests.get(link)

    print(f.text)
    c = f.text
    d = c.find("<title>")
    train = ""
    for i in range(d + 8, 1000):
        if f.text[i] == '-':
            break
        train = train + f.text[i]
    print(train)

    tts = gTTS(text=train, lang='en-us')
    tts.save("hel.mp3")
    os.system("hel.mp3")
    return train

def saynews():
    link = "https://news.google.com/news/?ned=in&gl=IN&hl=en-IN"
    f = requests.get(link)

    a = f.text
    news = ''
    b = a.find('jsname="NV4Anc" role="heading" aria-level="2"')

    regex = r'jsname="NV4Anc" role="heading" aria-level="2"(.+?)<'
    newslist = re.findall(regex, a)
    print(newslist)
    newsfin = ''
    for i in range(0, 2):
        newstr = newslist[i].replace(">", "")
        newstr2 = newstr.replace("&#39;", "'")
        newsfin = newsfin + '     ;' + newstr2
    newsfin = 'here are the latest top stories for now  ' + newsfin
    tts = gTTS(text=newsfin, lang='en-us')
    tts.save("hel.mp3")
    os.system("mpg321 hel.mp3")
    return newsfin


def saycricket():
    link = "http://www.cricbuzz.com/"
    new = 2
    f = requests.get(link)

    a = f.text
    b = a.find('cb-col cb-col-25 cb-mtch-blk')
    c = a.find('"_self" class="cb-font-12"><div class="cb-hmscg-bat-txt cb-ovr-flo ">')
    d = a.find('/div></div><div class="cb-hmscg-bwl-txt')
    team = ""
    for i in range(40, 100):
        if f.text[b + i] == '"':
            break
        team = team + f.text[b + i]

    print(team)
    team1 = ""
    for i in range(108, 150):
        if f.text[c + i] == '<':
            break
        team1 = team1 + f.text[c + i]
    print(team1)

    score1 = ""
    for i in range(183, 800):
        if f.text[c + i] == '<' or f.text[c + i] == 'O':
            break
        score1 = score1 + f.text[c + i]
    print(score1)

    team2 = ""
    for i in range(81, 800):
        if f.text[d + i] == '<':
            break
        team2 = team2 + f.text[d + i]
    print(team2)

    score2 = ""
    for i in range(155, 800):
        if f.text[d + i] == '<':
            break
        score2 = score2 + f.text[d + i]
    print(score2)
    if team1 == "RSA":
        team1 = "southafrica"
    if team1 == "AUS":
        team1 = "australia"
    if team1 == "BAN":
        team1 = "bangladesh"
    if team1 == "SL":
        team1 = "srilanka"
    if team1 == "NZ":
        team1 = "new zealand"
    if team1 == "ENG":
        team1 = "england"
    if team1 == "ZIM":
        team1 = "zimbabwe"
    if team1 == "IRE":
        team1 = "ireland"
    if team1 == "WI":
        team1 = "west indies"
    if team1 == "AUS":
        team1 = "australia"
    if team1 == "PAK":
        team1 = "pakistan"
    if team1 == "AFG":
        team1 = "afghanistan"
    if team1 == "IND":
        team1 = "india"

    if team2 == "RSA":
        team2 = "south africa"
    if team2 == "AUS":
        team2 = "australia"
    if team2 == "BAN":
        team2 = "bangladesh"
    if team2 == "SL":
        team2 = "srilanka"
    if team2 == "NZ":
        team2 = "new zealand"
    if team2 == "ENG":
        team2 = "england"
    if team2 == "ZIM":
        team2 = "zimbabwe"
    if team2 == "IRE":
        team2 = "ireland"
    if team2 == "WI":
        team2 = "west indies"
    if team2 == "AUS":
        team2 = "australia"
    if team2 == "PAK":
        team2 = "pakistan"
    if team2 == "AFG":
        team2 = "afghanistan"
    if team2 == "IND":
        team2 = "india"

    team = team.replace(" v ", " vs ")
    score1 = score1.replace("/", " for ")
    score1 = score1.replace(".", " point ")
    score1 = score1.replace("(", " in ")

    score2 = score2.replace("/", " for ")
    score2 = score2.replace(".", " point ")
    score2 = score2.replace("(", " in ")
    score2 = score2.replace(">", " ")
    score2 = score2.replace("Ovs", "overs ")
    team2 = team2.replace("RSA", "southafrica")
    team2 = team2.replace(">", "")

    output = team + "    " + team1 + "    " + "scored" + "    " + score1 + "overs" + "       " + team2 + "    " + "scored" + "     " + score2

    tts = gTTS(text=output, lang='en-us')
    tts.save("hel.mp3")
    os.system("mpg321 hel.mp3")
    return output


def priceof(term):
    tabUrl = "https://www.flipkart.com/search?q=";
    link = tabUrl + term
    f = requests.get(link)
    new = 2

    # webbrowser.open(tabUrl+term,new=new)
    # print(f.text)
    a = f.text
    b = a.find("1vC4OE _2rQ-NK")
    c = a.find("_3wU53n")
    p = a.find('_1vC4OE"')
    # print(p)
    if b == -1:
        b = a.find('1vC4OE')
        c = a.find("_2cLu-l")
        # print(b)
        # print(c)
        name = ""
        for i in range(16, 100):

            if f.text[c + i] == '<' or f.text[c + i] == '>' or f.text[c + i] == '"':
                break
            name = name + f.text[c + i]
        # print(name)
        price = ""
        for i in range(18, 120):
            if a[p + i] == '<':
                break

            price = price + a[p + i]
        # print(price)
        if price == 'refetch':
            output = "NO RESULTS FOUND FOR YOUR QUERY"
            print(output)
            tts = gTTS(text=output, lang='en-us')
            tts.save("hel.mp3")
            os.system("mpg321 hel.mp3")

        else:

            output = name + " costs " + price + " rupees"
            print(output)

            tts = gTTS(text=output, lang='en-us')
            tts.save("hel.mp3")
            os.system("mpg321 hel.mp3")

    else:
        # print(b)
        # print(c)
        name = ""
        for i in range(9, 130):
            if f.text[c + i] == '<':
                break

            name = name + f.text[c + i]

        # print(name)
        price = ""
        for i in range(25, 120):
            if a[b + i] == '<':
                break

            price = price + a[b + i]
            # print(price)
        output = name + " costs " + price + " rupees"
        print(output)

        tts = gTTS(text=output, lang='en-us')
        tts.save("hel.mp3")
        os.system("mpg321 hel.mp3")
    return output