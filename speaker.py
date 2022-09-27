import os
import playsound
import settings
from gtts import gTTS

def say (string):
    myobj = gTTS(text=string, lang=settings.getLanguage(), slow=False)
    myobj.save("audio.mp3")
    #os.system("audio.mp3")
    playsound.playsound('audio.mp3')
    os.remove('audio.mp3')