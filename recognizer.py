import speech_recognition as sr
import settings
import translator

# Function to capture audio
def microphone():
    with sr.Microphone() as source:
        audio = sr.Recognizer().listen(source)
        return(audio)

# Function to transcribe the audio to a string using Google
def transcription(audio):
    try:
        transcription = sr.Recognizer().recognize_google(audio, language=settings.getLanguage())
        return translator.translationToEnglish(transcription)
    except sr.UnknownValueError:
        return "I'm sorry I didn't understand you"