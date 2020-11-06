import pyttsx3#pip install pyttsx3
import datetime
import speech_recognition as sr#pip install speechRecognition
import wikipedia#pip install wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning boss")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon boss")
    else:
        speak("Good Evening boss")
    
    
    
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognising....")
        query  = r.recognize_google(audio)
        print("User said:",query)
    except Exception as e:
        #print(e)
          
        print("Say that again please....")
        return "None"
    return query

speak("Hi sir I am Jessica How may I help you")
wishMe()
while True:
    query = takeCommand().lower()
    
    if 'wikipedia' in query:
        speak("searching wikipedia...")
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query,sentences=2)
        speak("According to wikipedia")
        speak(results)
        #print(results)

    elif "open youtube" in query:
        webbrowser.open("youtube.com")

    elif "open google" in query:
        webbrowser.open("google.com")

    elif "play music" in query:
        music_dir = "C:\\Users\\munna\\Music"
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir, songs[0]))

    elif "open code editor" in query:
        code_path = "C:\\Users\\munna\\FLASK_projects\\Sublime Text 3\\sublime_text.exe"
        os.startfile(code_path)
        
    elif "the time" in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {strTime}")
        
    elif "open prime video" in query:
        webbrowser.open("primevideo.com")
    
