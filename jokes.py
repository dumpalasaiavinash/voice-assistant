from gtts import gTTS
import os
import speech_recognition as sr
import random
def tell_a_joke():
    joke = [
        "My friend thinks he is smart.He told me an onion is the only food that makes you cry,so i threw a coconut on his face.",
        "Is google male or female.Female,because it doesn't let you finish a sentence before making a suggestion.",
        "I have always thought my neighbours were quiet nice people.But then they put a password on their Wi-Fi",
        "I fear my neighbour may be stalking me,she's been googling my name last night on her computer.I saw it clearly through my binoculars.",
        "Anton,do you think i'm a bad mother?My name is paul."]
    a=random.randint(0,4)
    tts = gTTS(text=joke[a],lang='en-us')
    tts.save("hel.mp3")
    os.system("mpg321 hel.mp3")


