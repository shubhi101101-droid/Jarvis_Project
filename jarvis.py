import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import time

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
    engine.stop()
    time.sleep(0.3)

def processcomand(c):
    c = c.lower()

    if "open youtube" in c:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "open google" in c:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open spotify" in c:
        speak("Opening Spotify")
        webbrowser.open("https://www.spotify.com")

    elif c.startswith("play"):
        song = c.split(" ", 1)[1]

        if song in musicLibrary.music:
            speak(f"Playing {song}")
            webbrowser.open(musicLibrary.music[song])
        else:
            speak("Sorry, song not found")

if __name__ == "__main__":
    speak("Initializing Jarvis")

    while True:
        r = recognizer
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=3, phrase_time_limit=2)

            word = r.recognize_google(audio)

            if word.lower() == "jarvis":
                speak("Yes boss")
                time.sleep(0.5)

                with sr.Microphone() as source:
                    print("Jarvis active...")
                    audio = r.listen(source)

                command = r.recognize_google(audio)
                processcomand(command)

        except Exception as e:
            print("Could not understand audio;", e)
