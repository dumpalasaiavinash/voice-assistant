import requests
import re
from gtts import gTTS
import os

link="https://news.google.com/news/?ned=in&gl=IN&hl=en-IN"
f = requests.get(link)

a=f.text
news=''
b=a.find('jsname="NV4Anc" role="heading" aria-level="2"')



regex = r'jsname="NV4Anc" role="heading" aria-level="2"(.+?)<'
#line = "President [P] Barack Obama [/P] met Microsoft founder [P] Bill Gates [/P], yesterday."
newslist = re.findall(regex,a )
print(newslist)
newsfin=''
for i in range(0,5):
    newstr = newslist[i].replace(">", "")
    newstr2 = newstr.replace("&#39;", "'")
    newsfin=newsfin+'     ;'+newstr2
newsfin='here are the latest top stories for now  '+newsfin
tts = gTTS(text=newsfin, lang='en-us')
tts.save("hel.mp3")
os.system("mpg321 hel.mp3")
