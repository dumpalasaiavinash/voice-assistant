import pymysql
from gtts import gTTS
import os
import speech_recognition as sr
import time
db=pymysql.connect("den1.mysql2.gear.host","alasya2","alasya2.0","alasya2")
def talk(u):
 tts = gTTS(text=u, lang='en-us')
 tts.save("hel.mp3")
 os.system("mpg321 hel.mp3")
def talk1(u):
 tts = gTTS(text=u, lang='en-us')
 tts.save("helll.mp3")
 os.system("mpg321 helll.mp3")

def recognize():
 try:
  r = sr.Recognizer()
  with sr.Microphone() as source:
   audio = r.listen(source)
  output = r.recognize_google(audio)
  return output
 except:
  output=recognize()
  return output

def recognize1():
 try:
  r = sr.Recognizer()
  with sr.Microphone() as source:
   audio = r.listen(source)
  output = r.recognize_google(audio)
  return output
 except:
  output=''
  return output

def main():
 db = pymysql.connect("den1.mysql2.gear.host", "alasya2", "alasya2.0", "alasya2")
 temp1=1
 temp2=1
 temp3=1
 while(temp1==1):
  talk("Login or Register")
  output=recognize()
  print("You said: " + output)
  temp1=0
  if(output!='register'):
   if(output!='login'):
    talk1("I didn't get it exactly , come again")
    time.sleep(2)
    temp1=1

 temp1=1
 if(output=='register'):
  while(temp1==1):
   temp3=1
   talk("Username please")
   name=recognize()
   print("You said: " + name)
   temp = db.cursor()
   temp.execute("SELECT name1,name2 FROM contacts")
   check = temp.fetchall()
   for user,user1 in check:
    if(user==name or user1==name):
     talk("Username already exists , try a new one")
     temp3=0
     break
   if(temp3==1):
    temp1=0
  talk("Password please")
  password=recognize()
  print("You said: " + password)
  insert = db.cursor()
  insert.execute("INSERT INTO contacts (name1,name2) VALUES('" + name + "','" + password + "');")
  db.commit()
  insert.close()

 elif(output=='login'):
  while(temp2==1):
   talk("Username")
   user = recognize()
   print("You said: " + user)
   temp1=1
   temp3=1
   talk("Password")
   password = recognize()
   print("You said: " + password)
   temp = db.cursor()
   temp.execute("SELECT name1,name2 FROM contacts")
   check = temp.fetchall()
   for username,pas in check:
    if(user==username):
     temp1=0
     if(password==pas):
      temp3=0
      temp2=0
      break
   if(temp1==1):
    talk1("Username does not exist")
   elif(temp1==0 and temp3==1):
    talk1("Password does not match")
 temp1=1
 while (temp1 == 1):
  talk("With whom you want to chat")
  friend = recognize()
  print("You said: " + friend)
  temp = db.cursor()
  temp.execute("SELECT name1 FROM contacts")
  check = temp.fetchall()
  for name in check:
   name= ''.join(name)
   if (name == friend):
    temp1 = 0
    break
  if (temp1 == 1):
   talk("That user does not have an account , try another name please")
   time.sleep(3)
 temp4=0;temp5=0
 no1=0
 no2=0
 temp=db.cursor()
 temp.execute("SELECT name1,name2,text1,text2 FROM contacts")
 check=temp.fetchall()
 for f,k,i,j in check:
  if(j=='' and k==user and f==friend) :
   print(i)
   no1+=1
  if(j=='' and k==friend and f==user):
   print(' '*40,end='')
   print(i)
   no2+=1
 temp.close()
 temp6 = 0
 temp5=0
 while(temp4!=1):
  temp=db.cursor()
  temp.execute("SELECT * FROM contacts")
  check = temp.fetchall()
  num1=0
  num2=0
  for f, w, i, j in check:
   if (j == '' and w == user and f == friend):
    if(no1<num1):
     no1+=1
     print(i)
    num1 += 1
   if (j == '' and w == friend and f == user):
    if(no2<num2):
     no2+=1
     print(' ' * 40, end='')
     print(i)
    num2 += 1
   temp.close()
  if(temp5!=0 and message!=''):
   temp6=1
   check = db.cursor()
   check.execute("INSERT INTO contacts (name1,name2,text1,text2) VALUES('" + user + "','" + friend + "','" + message + "',' ');")
   check.execute("SELECT text1,text2 FROM contacts")
   z=check.fetchall()
   for i,j in z:
    x=i
   print(' '*40,end='')
   print(x)
   check.close()
  db.commit()
  if(temp6==0):
   talk("Message here")
   temp6=1
  message = recognize1()
  temp5+=1
  if(message=="hey buddy stop"):
   talk("Bye")
   break

db.close()
