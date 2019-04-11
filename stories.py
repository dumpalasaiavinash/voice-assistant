from gtts import gTTS
import os
import speech_recognition as sr
import random
def tell_a_story():
    stories=['Once upon a time, there lived a worm who dreamed of becoming a beautiful horse so that he could gallop in the grassy hills with his other horsey friends. One day he met a wizard frog.',"the lowly clerck was caught red handed for accepting bribe.miles away at home his wife waited for her husband to bring the money for her daughters cancer treatment.","Is google male or female.Female,because it doesn't let you finish a sentence before making a suggestion.","once a 5 year old boy was standing barefooted in the shallow water of the ocean.he kept repeating the same sentence to waves even when you touch my feet a thousand times i wont for","everyone goes with the flow but the one who goes against the flow becomes someone remarkable in life.before i could explain this to the traffic police,that guy issued me a challan."]
    a=random.randint(0,4)
    tts = gTTS(text=stories[a],lang='en-us')
    tts.save("hel.mp3")
    os.system("mpg321 hel.mp3")