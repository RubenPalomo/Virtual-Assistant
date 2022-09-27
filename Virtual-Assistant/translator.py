import googletrans

# Function to translate the string using Google
def translation(string, lang):
    translator = googletrans.Translator()
    return translator.translate(string.lower(), dest=lang).text.replace("tocando", "reproduciendo").replace("jugando", "reproduciendo")

# Function to translate to English
def translationToEnglish(string):
    translator = googletrans.Translator()
    return translator.translate(string.lower(), dest="en").text.replace("reproduce", "play")