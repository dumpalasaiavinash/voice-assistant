def add_to_shopping_list(item):
    fp = open('a.txt', 'a')
    fp.write(item + '\n')
    fp.close()
def read_shopping_list():
    fp = open('a.txt', 'r')
    data = fp.readlines()

    for line in data:
        tts = gTTS(text=line, lang='en-us')
        tts.save("hel.mp3")
        os.system("mpg321 hel.mp3")
    fp.close()


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


def new_shopping_list:
    tts = gTTS(text="the previous contents gets deleted,say yes to continue", lang='en-us')
    tts.save("hel.mp3")
    os.system("mpg321 hel.mp3")
    choice1 = sr.Recognizer()
    with sr.Microphone() as source:
        audio = choice1.listen(source)
    print("You said: " + choice1.recognize_google(audio))
    if (choice1.recognize_google(audio) == 'yes'):
        delete_shopping_list()


