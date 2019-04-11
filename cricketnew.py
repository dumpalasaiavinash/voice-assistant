import requests
import webbrowser
from gtts import gTTS
import os


link="http://www.cricbuzz.com/"
new=2
#webbrowser.open(link,new=new)

f = requests.get(link)

#print(f.text)
a=f.text
b=a.find('cb-col cb-col-25 cb-mtch-blk')
c=a.find('"_self" class="cb-font-12"><div class="cb-hmscg-bat-txt cb-ovr-flo ">')
d=a.find('/div></div><div class="cb-hmscg-bwl-txt')
#print(d)
#print(c)
#print(b)

team=""
for i in range(40,100):
    if  f.text[b+i] == '"':
        break
    team=team + f.text[b+i]

print(team)
team1=""
for i in range(108,150):
    if  f.text[c+i] == '<':
        break
    team1=team1 + f.text[c+i]
print(team1)

score1=""
for i in range(183,800):
    if  f.text[c+i] == '<' or f.text[c+i] == 'O':
        break
    score1=score1 + f.text[c+i]
print(score1)


team2=""
for i in range(81,800):
    if  f.text[d+i] == '<':
        break
    team2=team2 + f.text[d+i]
print(team2)

score2=""
for i in range(155,800):
    if  f.text[d+i] == '<':
        break
    score2=score2 + f.text[d+i]
print(score2)
if team1=="RSA":
    team1 = "southafrica"
if team1=="AUS":
    team1 = "australia"
if team1=="BAN":
    team1 = "bangladesh"
if team1=="SL":
    team1 = "srilanka"
if team1=="NZ":
    team1 = "new zealand"
if team1=="ENG":
    team1 = "england"
if team1=="ZIM":
    team1 = "zimbabwe"
if team1=="IRE":
    team1 = "ireland"
if team1=="WI":
    team1 = "west indies"
if team1=="AUS":
    team1 = "australia"
if team1=="PAK":
    team1 = "pakistan"
if team1=="AFG":
    team1 = "afghanistan"
if team1=="IND":
    team1 = "india"



if team2=="RSA":
    team2 = "south africa"
if team2=="AUS":
    team2 = "australia"
if team2=="BAN":
    team2 = "bangladesh"
if team2=="SL":
    team2 = "srilanka"
if team2=="NZ":
    team2 = "new zealand"
if team2=="ENG":
    team2 = "england"
if team2=="ZIM":
    team2 = "zimbabwe"
if team2=="IRE":
    team2 = "ireland"
if team2=="WI":
    team2 = "west indies"
if team2=="AUS":
    team2 = "australia"
if team2=="PAK":
    team2 = "pakistan"
if team2=="AFG":
    team2 = "afghanistan"
if team2=="IND":
    team2 = "india"



team = team.replace(" v "," vs ")
score1=score1.replace("/"," for ")
score1=score1.replace("."," point ")
score1=score1.replace("("," in ")

score2=score2.replace("/"," for ")
score2=score2.replace("."," point ")
score2=score2.replace("("," in ")
score2=score2.replace("Ovs" ,"overs ")
team2=team2.replace("RSA","southafrica")
team2=team2.replace(">","")

output = team + "    "+  team1  + "    "+ "scored" + "    "+ score1  + "overs" + "       "+ team2 + "    " + "scored" + "     "+ score2

tts = gTTS(text=output, lang='en-us')
tts.save("hell.mp3")
os.system("mpg321 hel.mp3")
