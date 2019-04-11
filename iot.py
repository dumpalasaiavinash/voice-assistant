import requests
from gtts import gTTS
import os

tabUrl="https://api.thingspeak.com/update?api_key=OXA7CKWIHWFMPSZV&field1=143";

link=tabUrl
f = requests.get(link)
print(f.text)