import requests
from gtts import gTTS
import os

address=input("enter the location: ")
api_key = "AIzaSyC-PM-difZHAVazccuVY0jymsI-sgvugqg"
api_response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}'.format(address, api_key))
api_response_dict = api_response.json()

if api_response_dict['status'] == 'OK':
    latitude = api_response_dict['results'][0]['geometry']['location']['lat']
    longitude = api_response_dict['results'][0]['geometry']['location']['lng']
    print ('Latitude:', latitude)
    print ('Longitude:', longitude)

lat=str(latitude) + ',' + str(longitude)
print(lat)
lin="https://weather.com/en-IN/weather/today/l/"
link=lin +  lat
f = requests.get(link)
#print(f.text)
a=f.text
b=a.find('<span class="styles-xz0ANuUJ__temperature__3Ph8k">')
#print(b)
temp=""
for i in range(50,53):
    if f.text[b+i] == '<':
        break
    temp=temp + f.text[b+i]

output="the temperature at " + address + "is" + temp +" degree centigrade"
print(temp+" degree centigrade")

tts = gTTS(text=output, lang='en-us')
tts.save("hel.mp3")
os.system("mpg321 hel.mp3")
