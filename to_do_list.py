def add_to_to_do_list(item):
    fp=open('b.txt','a')
    fp.write(item + '\n')
    fp.close()
def read_to_do_list():
    fp=open('b.txt','r')
    data=fp.readlines()

    for line in data:
        tts = gTTS(text=line,lang='en-us')
        tts.save("hel.mp3")
        os.system("mpg321 hel.mp3")
    fp.close()
def delete_to_do_list():
    fp= open('b.txt', 'r+')
    fp.truncate()
    fp.close()
def delete_from_to_do_list(item):
    fp= open("b.txt", "r")
    d = fp.readlines()
    fp.close()
    fp=open("b.txt","w")
    for line in d:
        if item not in line:
            fp.write(line)
    fp.close()
def new_to_do_list:
    tts = gTTS(text="the previous contents gets deleted,say yes to continue", lang='en-us')
    tts.save("hel.mp3")
    os.system("mpg321 hel.mp3")
    choice = sr.Recognizer()
    with sr.Microphone() as source:
        audio = choice.listen(source)
    print("You said: " + choice.recognize_google(audio))
    if(choice.recognize_google(audio)=='yes'):
        delete_to_do_list()


