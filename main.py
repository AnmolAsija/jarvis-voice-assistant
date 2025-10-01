import speech_recognition as sr  ## speech to text
import webbrowser
import pyttsx3   ## text to speech
import musiclibrary
#import requests

# pip install pocketsphinx


# now we create a recognizer object
recognizer = sr.Recognizer()
engine = pyttsx3.init()
#newsapi = "261bdf410ede4f4c81865d5296a10145"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processcommand(c):
    if "open google " in c.lower():
        webbrowser.open("http://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("http://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("http://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("http://linkedin.com")
    elif c.lower().startswith("play"):
       song = c.lower().split(" ")[1]
       link =  musiclibrary.music[song]
       webbrowser.open(link)
    # elif "news" in c.lower():
    #      r = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=261bdf410ede4f4c81865d5296a10145")
    # else:
    #     # Let OpenAI handle the request       # required paid 
    #     pass

    

if __name__ == "__main__":# use this...so that.. when we call jarvis...it can only listen at that time
    speak("Initializing Jarvis......")

    while True:
        # Listen for the Wake word "jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
       
        # recognize speech 
        print("recognizing...")
        try:                         
            with sr.Microphone() as source:   # phrase_time or timeout error na aae...esliya try me lakr gae
                print("Listening...")
                audio = r.listen(source , timeout=2)#, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower()=="jarvis"):
                speak("Ya")
                # Listen for command
                with sr.Microphone() as source:   # phrase_time or timeout error na aae...esliya try me lakr gae
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    processcommand(command)



        except Exception as e:
            print("Error; {0}".format(e))
