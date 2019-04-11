import functionset
import speech_recognition as sr
import random
import PyDictionary
from graphics import *
import basicdb2
import rps
import singlebus
import no
import jokes
import stories
import trainnumber

win = GraphWin("buddy", 400, 600)
img = Image(Point(199, 300), "back2.gif")
img.draw(win)

l = ["", "", "", "", "", "", "", "", "", ""]
p = ["", "", "", "", "", "", "", "", "", ""]
e = ["", "", "", "", "", "", "", "", "", ""]

while True:
    x = 1
    y = 600
    click=win.checkMouse()
    temp=0
    while click==None:
        click=win.checkMouse()
        if(click==None):
            continue
        else:
            if((510<click.y<575) and (170<click.x<235)):
                temp=1
                click=click
            elif((560<click.y<590) and (360<click.x<390)):
                click=click
            else:
                click=None

    if((560<click.y<590) and (360<click.x<390)):
        img = Image(Point(199, 300), "info.gif")
        img.draw(win)
        click = win.checkMouse()
        while click == None:
            click = win.checkMouse()
            if (click == None):
                continue
            else:
                if ((550 < click.y < 590) and (350 < click.x < 380)):
                    click = click
                elif ((510 < click.y < 575) and (170 < click.x < 235)):
                    click = click
                    temp=1
                else:
                    click = None
        img = Image(Point(199, 300), "back2.gif")
        img.draw(win)

    if(temp==1):
        try:
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    print("Say something!")
                    audio = r.listen(source)
                res = r.recognize_google(audio)
                print("You said: " + res)
                l = [res] + l
        except:
            functionset.sayout('sorry. I did not get you')
            exception='sorry. I did not get you'
            res=''

        ######## RECOGNITION ALGORITHM STARTS HERE
        
        if 'hey' in res and 'Siri' in res:
            functionset.sayout('who is siri?')
            try:
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    print("Say something!")
                    audio = r.listen(source)
                res = r.recognize_google(audio)
                print("You said: " + res)
                functionset.sayout('who is that siri?')
                try:
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
                        print("Say something!")
                        audio = r.listen(source)
                    res = r.recognize_google(audio)
                    print("You said: " + res)
                    functionset.sayout('you better go and ask "siri". bye')
                    opt='you better go and ask "siri". bye'
                except:
                    functionset.sayout('you better go and ask "siri". bye')
                    opt='you better go and ask "siri". bye'
            except:
                functionset.sayout('I am asking you who is "siri"')
                try:
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
                        print("Say something!")
                        audio = r.listen(source)
                    res = r.recognize_google(audio)
                    print("You said: " + res)
                    functionset.sayout('who is that siri?')
                    opt='who is that siri?'
                    try:
                        r = sr.Recognizer()
                        with sr.Microphone() as source:
                            print("Say something!")
                            audio = r.listen(source)
                        res = r.recognize_google(audio)
                        print("You said: " + res)
                        functionset.sayout('you better go and ask "siri". bye')
                        opt='you better go and     ask "siri". bye'
                    except:
                        functionset.sayout('you better go and ask "siri". bye')
                        opt='you better go and     ask "siri". bye'
                except:
                    functionset.sayout('bye!')
                    opt='bye!'
        elif 'weather' in res or 'temperature' in res or 'climate' in res or 'how hot' in res or 'how cold' in res:
            res = functionset.genkeyw(res)
            res = res - {'temperature', 'climate', 'weather', 'hot', 'cold', 'hi', 'hello', 'here'}
            if len(res) == 0:
                res = 'sri city'
            res = str(res)
            print(res)
            opt=functionset.sayweather(res)
        elif 'time' in res and ('what' in res or 'can you tell me' in res):
            opt=functionset.time()
        elif 'date' in res:
            opt=functionset.date()
        elif 'which' in res and 'day' in res and 'today' in res:
            opt=functionset.day()
        elif 'price' in res or 'rate' in res or 'how much' in res or 'cost' in res or 'costs' in res:
            res = functionset.genkeyw(res)
            res = res - {'cost', 'costs', 'rate', 'price', 'much', 'flipkart', 'amazon'}
            res = str(res)
            opt=functionset.priceof(res)
        elif 'news' in res or 'happening' in res or 'happenings' in res or 'going on' in res:
            opt=functionset.saynews()
        elif res == 'hello' or res == 'hi' or res == 'hello buddy' or res == 'hi buddy':
            option2 = ['hi', 'hello dear', 'hello', 'namaste', 'namaskaar']
            opt = option2[random.randint(0, 4)]
            functionset.sayout(opt)
            print(opt)
        elif 'how do you do' in res:
            opt = 'how do you do?'
            functionset.sayout(opt)
        elif 'what' in res and 'you' in res and ('doing' in res or 'feeling' in res):
            option1 = ['i am always intrested to learn new thing. would you like to hear to an intresting fact?',
                       'just having a laugh. would you like to listen to a joke?', 'i am bored.wondering what to do']
            opt = option1[random.randint(0, 2)]
            functionset.sayout(opt)
        elif 'how are you' in res:
            option1 = ['i am great. thanks for asking', 'i am having a great day. thanks for asking']
            opt = option1[random.randint(0, 1)]
            functionset.sayout(opt)
        elif 'I' in res and ('bored' in res or 'bore' in res):
            opt = 'I am bored too. Shall we play a game?'
            functionset.sayout(opt)
        elif 'what' in res and 'can' in res and 'you' in res and 'do' in res:
            opt = 'here are the things i can do for you.  create a shopping list or a to-do list for you, help chat with your friend, tell stories, play music , tell you the weather conditions, search for the prices of goods on flipkart, play a game ,tell a joke, tell the news,and i can ask some riddles too'
            functionset.sayout(opt)
        elif ('who' in res or 'why' in res) and 'made' in res and 'you' in res:
            opt = 'i was made by the alasya group as a part of their ITWS2 software project'
            functionset.sayout(opt)
        elif 'introduce' in res or 'introduction' in res:
            opt = 'hello! i am the voice assistant created by alasya group. you can call me "buddy". here are the things i can do. i can create a shopping list or a to-do list for you, help chat with your friend, tell stories, play music , tell you the weather conditions, search for the prices of goods on flipkart, play a game ,tell a joke, tell the news,and i can ask some riddles too '
            functionset.sayout(opt)
        elif ('how old' in res and 'you' in res) or ('your age' in res and ('what is' in res or "what's" in res)) or (
                'when' in res and 'you' in res and 'born' in res):
            opt = 'what would you do with "my" age?'
            functionset.sayout(opt)
        elif res == 'Hey buddy' or res == 'hey' or res == 'buddy':
            opt = 'hey! hi. what can i do for you?'
            functionset.sayout(opt)
        elif 'language' in res and 'you' in res and 'speak' in res:
            opt = 'English for now'
            functionset.sayout(opt)
        elif 'you' in res and 'like' in res and 'what' in res:
            option1 = ['I like talking with you', 'i am always interested in learning new things',
                       'Serving you gives me a great pleasure']
            opt = option1[random.randint(0, 2)]
            functionset.sayout(opt)
        elif 'who' in res and 'are' in res and 'you' in res:
            opt = 'i am buddy! the voice assistant designed by alasya team'
            functionset.sayout(opt)
        elif 'where' in res and 'are' in res and 'you' in res:
            opt = 'i am here! right in front of you.'
            functionset.sayout(opt)
        elif ('tell' in res or 'say' in res) and ('fact' in res or 'interesting fact' in res):
            opt = functionset.ask_a_riddle()
        elif 'riddle' in res and ('ask' in res or 'tell' in res):
            opt = functionset.ask_a_riddle()
        elif ('cricket' in res and 'score' in res) or 'scored' in res or ('IPL' in res and 'score' in res):
            opt=functionset.saycricket()
        elif ('play' in res and ('music' in res or 'songs' in res) and len(res)==2) or res=='play a song' or ('play' in res and 'random' in res):
            functionset.sayout('palying a ramdom track')
            functionset.playrandom()
            opt='playing a random track'
        elif('joke' in res):
            jokes.tell_a_joke()
            opt='What else can I do for you'
        elif("status"in res or "Status" in res and ("Train" in res or "train" in res)):
            trainnumber.trainno()
            opt="Any other"
        elif ('stories' in res or 'story' in res or 'Story' in res or 'Stories' in res):
            stories.tell_a_story()
            opt = 'What else can I do for you'
        elif 'start' in res and 'chat' in res:
            basicdb2.main()
            opt='What else can I do for you'
        elif 'shopping list' in res and 'add' in res:
            res=functionset.genkeyw(res)
            res = res - {'shopping', 'list', 'add', 'my'}
            res = str(res)
            functionset.add_to_shopping_list(res)
            opt = 'i have added '+res+'  to your shopping list '
            functionset.sayout(opt)
        elif 'what' in res and 'in' in res and 'shopping list' in res:
            opt=functionset.read_shopping_list()
        elif 'play' in res and ('rock' in res or 'Rock' in res) and ('paper' in res or 'Paper' in res) and  ('scissors' in res or 'Scissors' in res) :
            rps.rockpaperscissors()
            opt='Wanna try anything else'
        elif 'play' in res and ('bus' in res or 'Bus' in res) or ('Buzz' in res or 'buzz' in res):
            singlebus.busbuzz()
            opt='Wanna try anything else'
        elif 'play' in res and ('number' in res or 'Number' in res):
            no.numbergame()
            opt='Wanna try anything else'

        elif ('videos' in res and 'show' in res) or (('show' in res or 'open' in res or 'play' in res or 'search for' in res) and 'YouTube' in res):
            res = functionset.genkeyw(res)
            res = res - {'YouTube','me','video','videos','in','on','of','some','about','open','play'}
            res =str(res)
            opt='here you go'
            functionset.sayout('here you go')
            functionset.youtube(res)
        elif 'meaning of' in res or 'mean' in res or 'means' in res or (len(res) == 3 and 'what' in res and 'is' in res):
            res = functionset.genkeyw(res)
            res = res - {'hi', 'hello', 'meaning', 'mean', 'means', 'do', 'does'}
            meaning = str(res)
            meaning = meaning[2:-2]
            print(meaning)
            dictionary = PyDictionary()
            x = dictionary.meaning(meaning)
            print(x)
        elif 'which' in res or 'what' in res or 'who' in res or 'why' in res or 'where' in res or 'how' in res or 'can you tell me' in res or 'when' in res:
            functionset.sayout('here are something what I found')
            opt='here are something what  I found'
            functionset.googleit(res)
        elif res=='' :
            l = [exception] + l
            opt=''
        else:
            opt = 'sorry! i cannot do that'
            functionset.sayout(opt)

        ######### GUI STARTS HERE ##########

        p=[opt]+p
        print(l)
        y = 450
        x = 200
        print(p)
        img=Image(Point(199,300), "back2.gif")
        img.draw(win)

        for i in range(0, 10):
            inp = Text(Point(x, y), e[i])
            inp.setSize(22)
            inp.setTextColor(color_rgb(40,125,200))
            inp.draw(win)
            y = y - 50
        y=450
        for i in range(0, 10):
            if(len(p[i])>30):
                q=p[i].split(' ')
                r=["","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""]
                for j in range(len(q)-1,-1,-1):
                    r[int(j/4)]=q[j]+" "+r[int(j/4)]
                for j in range(int(len(q)/4)-1,-1,-1):
                    inp = Text(Point(x, y), r[j])
                    inp.setSize(22)
                    y=y-25
                    inp.setTextColor(color_rgb(40, 125, 200))
                    inp.draw(win)

            else:
                inp = Text(Point(x, y), p[i])
                inp.setSize(22)
                inp.setTextColor(color_rgb(40,125,200))
                inp.draw(win)
                y = y - 50
            inp = Text(Point(x, y), l[i])
            inp.setSize(22)
            inp.setTextColor(color_rgb(40,125,0))
            inp.draw(win)
            y = y - 50

win.getMouse()