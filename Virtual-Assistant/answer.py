import pywhatkit
import requests
import json
import datetime
import settings
import wikipedia
import webbrowser
import pyjokes
import speaker
import translator

def reply(text):
    text = text.replace("sari", "")

    if (text == ""):
        return "Hi! Tell me what can I do for you"
    
    elif ("how" in text and ("are you doing" in text or "are you" in text or "are you doing" in text)):
        return "With the batteries charged!"

    elif ("hi " in text or "hello " in text):
        return "Hi! You are nice"

    # Reply to search on YouTube
    elif ("play" in text or "put me" in text or "youtube" in text):
        music = text.replace("play", "").replace("youtube", "")
        pywhatkit.playonyt(music)
        return "Playing " + music

    # Reply to search on Google
    elif ("google" in text):
        text = text.replace("look for", "").replace("search", "").replace("find", "").replace("me", "").replace("google", "")
        webbrowser.open("https://www.google.com/search?q=" + text,
                        new=2, autoraise=True)
        return "This is what I found on Google"

    # Reply to ask about the weather in a place
    elif ("weather" in text):
        # We need an api to access at the service
        api = "c9df8fe0664a7999de8d77b1ddf7759c"
        # First we get the city name that the user is requesting
        data = text.split(" ")
        i = data.index("in") + 1
        city = ""
        while i < len(data):
            city += data[i]
            i += 1
        # Then we have all the requeriments to get the weather information
        base_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}"
        response = requests.get(base_url).json()
        # If the response is a 429 code, we have exceeded the daily query limit
        if (response["cod"] == "429"):
            return "Daily query limit exceeded"
        # Else if we get the 404 code it means the city was not found
        elif (response["cod"] == "404"):
            return "The city you specified has not been found "
        else:
            # We have to transform the grades to celsius
            grades = (response["main"]["temp"] - 32) * 5 / 90
            # And then we have all the elements to respond
            return "It's a " + \
                response["weather"][0]["description"] + \
                    ", with " + str(round(grades)) + \
                    " degrees Celsius."

    # Reply to look for information in Wikipedia
    elif ("information" in text or "wikipedia" in text):
        wikipedia.set_lang(settings.getLanguage())
        try:
            text = text.replace("give me information about", "").replace("wikipedia", "")
            string = str(wikipedia.summary(text))
            speaker.say(translator.translation(
                "Searching information about " + text + ". This could take me a while."))
            return string
        except:
            text = text.replace("look for", "").replace("search", "").replace(
                "find", "").replace("give me information about", "").replace("wikipedia", "")
            pywhatkit.search(text)
            return "Searching " + text

    # Reply to look for information
    elif ("search" in text or "look for" in text or "find" in text):
        text = text.replace("look for", "").replace("search", "").replace("find", "")
        pywhatkit.search(text)
        return "Searching " + text
    
    # Reply to change the language
    elif ("change" in text and "language" in text):
        if ("english" in text):
            settings.setLanguage("en")
        elif ("spanish" in text):
            settings.setLanguage("es")
        elif ("french" in text):
            settings.setLanguage("fr")
        elif ("german" in text):
            settings.setLanguage("de")
        elif ("catalan" in text):
            settings.setLanguage("ca")
        else:
            return "Sorry, I didn't understand the language you want to change to"
        return "The language was changed successfully"

    # Reply to translate a word to another language
    elif ("translate" in text):
        language = ""
        if ("english" in text):
            language = "en"
        elif ("spanish" in text):
            language = "es"
        elif ("french" in text):
            language = "fr"
        elif ("german" in text):
            language = "de"
        elif ("catalan" in text):
            language = "ca"
        else:
            return "Sorry, I didn't understand the language you want to change to"
        text = text.replace("translate", "").replace("to english", "").replace(
            "to spanish", "").replace("to french", "").replace("to german", "").replace("to catalan", "")
        return "translate " + translator.translation(text, language)

    # Reply to ask what time is now
    elif ("hour" in text or "time" in text):
        return "It's " + str(datetime.datetime.now().hour) + ":" + str(datetime.datetime.now().minute)

    # Reply to ask what day is today
    elif ("today" in text):
        months = ("January", "February", "March", "April", "May", "June",
                  "July", "August", "September", "October", "November", "December")
        month = months[int(datetime.datetime.now().strftime('%m')) - 1]
        return "Today is " + datetime.datetime.now().strftime('%A') + " " + month + " " + str(
            datetime.datetime.now().day) + ", " + str(datetime.datetime.now().year)

    # Reply to show Sari's talent to sing
    elif ("sing" in text):
        speaker.say(translator.translation("I'm a great singer, listen:", settings.getLanguage()))
        reply = "Caramelo de chocolate Empápame así Como un pionono de vitrina Enróllame así Con azúcar en polvo, endúlzame"
        reply += " Y es que tú eres mi rey Qué lindo eres tú, eres mi bebé Mi bebito Fiu Fiu"
        return reply

    # Reply to create a note with all that we said
    elif ("annotate" in text or "write" in text or "note" in text or "score" in text or "point" in text):
        f = open("notes.txt", 'a')
        text = text.replace("write", "").replace("annnotate", "").replace("note", "").replace("score", "").replace("point", "")
        f.write(translator.translation(text, settings.getLanguage()) + "\n")
        return "A note has been added successfully. You can see it in my folder"

    # Reply to tell jokes
    elif ("joke" in text or "gag" in text):
        try:
            return pyjokes.get_joke(language=settings.getLanguage(), category="all")
        except:
            return translator.translation(pyjokes.get_joke(language="en", category="all"))

    # Reply to help the user by saying all the things Sari can do
    elif ("help" in text or "introduce yourself" in text or "present" in text):
        reply = "I'm Sari, your virtual assistant. I am able to tell you what day is today, what time is it, write notes if you "
        reply += "ask me to annotate it, translate words or sentences to another languages, search information in Google or Wikipedia,"
        reply += " play music on YouTube and much more!"
        return translator.translation(reply, settings.getLanguage())

    # Reply to ask the program for a pause
    elif ("wait" in text or "pause" in text or "stop" in text):
        return "Okay, let's get some rest. You can always call me back to help you again"

    elif ("thanks" in text or "thank you" in text):
        return "No problem. I am delighted to be able to help you"

    elif ("bye" in text or "leave" in text or "quit" in text):
        return "Goodbye! See you soon!"

    return "I'm sorry I didn't understand you"