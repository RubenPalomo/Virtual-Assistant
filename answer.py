import pywhatkit
import datetime

def reply(text):
    if ("how" in text and ("are you doing" in text or "are you" in text or "are you doing" in text)):
        return "With the batteries charged!"
    elif ("hi " in text or "hello " in text):
        return "Hi! You are nice"
    elif ("play" in text or "put" in text):
        music = text.replace("play", "")
        pywhatkit.playonyt(music)
        return "Playing " + music
    elif ("search" in text or "look for" in text or "find" in text):
        text = text.replace("look for", "").replace("search", "").replace("find", "")
        pywhatkit.search(text)
        return "Searching " + text
    elif ("information" in text):
        return str(pywhatkit.info(text, lines = 4))
    elif ("hour" in text or "time" in text):
        return "It's " + str(datetime.datetime.now().hour) + ":" + str(datetime.datetime.now().minute)
    elif ("today" in text):
        months = ("January", "February", "March", "April", "May", "June",
                  "July", "August", "September", "October", "November", "December")
        month = months[int(datetime.datetime.now().strftime('%m')) - 1]
        return "Today is " + datetime.datetime.now().strftime('%A') + " " + month + " " + str(datetime.datetime.now().day) + ", " + str(datetime.datetime.now().year)
    elif ("bye" in text or "leave" in text or "quit" in text):
        return "Goodbye! See you soon!"

    return "I'm sorry I didn't understand you"