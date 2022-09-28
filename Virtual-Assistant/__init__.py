import speaker
import settings
import tkinter
import recognizer
import answer
import translator
from colorama import *

exit = False
wait = False

# Function to choose the language and close the window
def chooseLanguage(lang):
    settings.setLanguage(lang)
    window.destroy()

# Function to center the window on the screen
def centerWindow(r):
    height = r.winfo_reqheight()
    width = r.winfo_reqwidth()
    screen_height = r.winfo_screenheight()
    screen_width = r.winfo_screenwidth()
    x = (screen_width//2) - (width//2)
    y = (screen_height//2) - (height//2)
    r.geometry(f"+{x}+{y}")

# Function to know when it should stop
def isTimeToStop(text):
    if ("exit" in text or "quit" in text or "leave" in text or "play" in text or "search" in text or "bye" in text or "thanks" in text):
        return True
    elif ("youtube" in text or "google" in text or "put me" in text):
        return True
    return False

# Function to pause the program and resume it when the user calls Sari
def isTimeToWait(text):
    global wait
    if ("ari" in text or "siri" in text):
        wait = False
    else:
        wait = True

# Function to exit
def finishSari():
    global exit
    exit = True
    print(Fore.CYAN + "BYE!!")

# We define the main function
def main():
    global exit
    while(not exit):
        global wait
        audio = recognizer.microphone()
        if (audio):
            text = recognizer.transcription(audio).lower()
            if (not wait):
                print(Fore.GREEN + text)
                reply = answer.reply(translator.translationToEnglish(text))
                if ("translate" in reply):
                    speaker.say(reply.replace("translate", ""))
                else:
                    speaker.say(translator.translation(reply, settings.getLanguage()))
                if ("rest" in reply):
                    wait = True
                if (isTimeToStop(text)):
                    finishSari()
            else:
                print(Fore.GREEN + text)
                isTimeToWait(text)
                if (not wait):
                    speaker.say(translator.translation(
                        "Hi again! What can I do for you?", settings.getLanguage()))

# Part of the graphical interface where there will be buttons that will be shown to the user to choose the language
window = tkinter.Tk()
centerWindow(window)
buttonEN = tkinter.Button(window, text="English",
                          command=lambda: chooseLanguage("en"))
buttonEN.pack()
buttonES = tkinter.Button(window, text="Español",
                          command=lambda: chooseLanguage("es"))
buttonES.pack()
buttonCA = tkinter.Button(window, text="Català",
                          command=lambda: chooseLanguage("ca"))
buttonCA.pack()
buttonFR = tkinter.Button(window, text="Française",
                          command=lambda: chooseLanguage("fr"))
buttonFR.pack()
buttonDE = tkinter.Button(window, text="Deutsche",
                          command=lambda: chooseLanguage("de"))
buttonDE.pack()
window.mainloop()

if __name__ == '__main__':
    if (settings.getLanguage() == ""):
        quit()
    print(Fore.YELLOW + "Listening...")
    speaker.say(
        translator.translation(
            "Hi! I am your virtual assistant. My name is Sari and I am delighted to help you.", settings.getLanguage()))
    speaker.say(
        translator.translation(
            "If you want to know more about me request me to introduce myself or ask me for help", settings.getLanguage()))
    main()