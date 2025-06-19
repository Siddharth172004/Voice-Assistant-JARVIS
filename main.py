import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests
import json
from client import get_ai_response

url = "https://api.deepseek.com/v1/chat/completions"
api = "a839b0262f3744c08c894e255c92d5e4"
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open ("https://google.com")
    elif "open linkedin" in c.lower():
        webbrowser.open ("https://linkedin.com")
    elif "open facebook" in c.lower():
        webbrowser.open ("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open ("https://youtube.com")
    elif "open chat gpt" in c.lower():
        webbrowser.open ("https://chatgpt.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?q=india&language=en&apiKey={api}")
        if r.status_code == 200:
                data = r.json()
                articles = data.get("articles", [])
                speak("Here are the top news headlines.")
                for article in articles[:5]:
                    speak(article["title"])
        else:
           speak("Sorry, I couldn't fetch the news.")

    else:
        
        reply = get_ai_response(c)
        speak(reply)


if __name__ == "__main__":
    speak("Initializing Jarvis......")
    while True:
        r = sr.Recognizer()
        print("Recognizing....")
        try:
            with sr.Microphone() as source:
                 print ("Listeniig...")
                 audio = r.listen(source, timeout=3, phrase_time_limit=5)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                  speak("Yes Sir")
                  with sr.Microphone() as source:
                      print("Jarvis Active...")
                      audio = r.listen(source)
                      commond = r.recognize_google(audio)

                      processCommand(commond)

        except Exception as e:
            print("Error ; {0}".format(e))

        
