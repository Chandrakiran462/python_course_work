import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser


engine = pyttsx3.init()
def speak(text):
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        recognizer.pause_threshold = 1

        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio,language='en-in')
            print("🗣️ You said:", command)
            return command.lower()
        except sr.UnknownValueError:
            print("❌ Sorry, I didn't understand.")
            speak("Sorry, I didn't catch that.")
            return ""
        except sr.RequestError:
            print("❌ Speech service error.")
            speak("Sorry, my speech service is down.")
            return ""
    
speak("Hi, this is Your virtual Assistant. How can I help you.")
def run_assistant():
    speak("Hello! I'm your virtual assistant. How can I help you?")
    while True:
        command = input()

        if 'play music' in command:
            speak("Opening Spotify")
            webbrowser.open("https://open.spotify.com/")

        elif 'reminder' in command:
            speak("reminder set to push code at 5pm")
    
        elif 'exit' or 'stop' or 'bye' in command:
            speak("okay, Have good day")
            break
        else:
            speak("I don't have that access yet.")

# Run the assistant
run_assistant()