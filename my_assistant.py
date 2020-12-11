import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pyjokes
import smtplib 
import json 
from urllib.request import urlopen

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
        
        
def sendEmail(to,content): 
    server = smtplib.SMTP('smtp.gmail.com',587) 
    server.ehlo() 
    server.starttls() 
    #Enable low security in gmail 
    server.login(#'baquarabbas12920@gmail.com','Abbas$@456') 
    server.sendmail(#'baquarabbas12920@gmail.com', to, content)
    server.close()
    
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognising....")
        query1  = r.recognize_google(audio)
        print("User said:",query)
        
    except Exception as e:
        #print(e)
          
        print("Say that again please....")
        return "None"
    return query1

speak("Hi sir I am Jessica How may I help you")
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
                  
    elif "open code editor" in query:
        code_path = "C:\\Users\\munna\\FLASK_projects\\Sublime Text 3\\sublime_text.exe"
        os.startfile(code_path)
    
    elif "the time" in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {strTime}")
        
    elif "open prime video" in query:
        webbrowser.open("primevideo.com")
   
    elif "play music" in query:
        music_dir = "C:\\Users\\munna\\Music"
        songs = os.listdir(music_dir)
        #print(songs)
        os.startfile(os.path.join(music_dir, songs[0])) 
    elif  "who are you" in query:
        speak("I am jessica your personal assistant") 
    
    elif "what can you do" in query:
        speak("I can do some tasks like I can open your favourite websites,I can get you some jokes,music and many more")
    
    elif "how are you"  in query:
        speak("Well,It is great to hear it from you") 
        speak("I am fine,Thank you sir") 
        speak("How are you?") 
        
    elif "fine" in query or "good" in query:
        speak("It is good to know that you are fine") 
        
    elif "joke" in query:
        speak(pyjokes.get_joke()) 
    
    elif "open netflix" in query:
        webbrowser.open("netflix.com") 
        
    elif "open imdb" in query:
        webbrowser.open("imdb.com") 
        
    elif "open google trends" in query:
        webbrowser.open("trends.google.com") 
    
    elif "open amazon" in query:
        webbrowser.open("amazon.com") 
        
    elif "open flipkart" in query:
        webbrowser.open("'flipkart.com")
    
    elif "open spotify" in query:
        webbrowser.open("spotify.com") 
    
    elif "who made you" or "who created you" in query:
        speak("I have been created by munna as part of his own project")
    
    elif "I love you" in query:
        speak("There is no gift better than love") 
    
    elif "love me" in query:
        speak("ofcourse,What would I do without you") 
        
    elif "send mail" in query: 
        try:
            speak("what should I say") 
            content = takeCommand() 
            speak("whoam should I send") 
            to = input("Enter your mail id: ")
            sendEmail(to, content) 
            speak('Email has been sent !') 
        except Exception as e:
            print(e) 
            speak('I am unable to send this email') 
            
    
    elif "wish" in query:
        wishMe() 
        
    elif "who am i" in query:
        speak("You are not an alien for sure,You are talking like a most-intelligent creature in this world") 
        speak("You are human!")
        
    elif "where is" in query:
        query = query.replace("where is", "") 
        location = query 
        speak("you askmed me to locate at") 
        speak(location) 
        webbrowser.open("https://www.google.nl/maps/place/" + location + " ") 
           
    elif "news" in query:
        try:
            jsonObj = urlopen("https://newsapi.org/v1/articles?source = the-times-of-india&sortBy = top&apiKey =05bd83c4995d427ea84f5d08291e5117")
            data = json.load(jsonObj)
            i = 1 
            speak("Here are the top news from times of India") 
            for item in data['articles']:
                print(str(i) + '. ' + item['title'] + '\n')
                print(item['description'] + '\n') 
                speak(str(i) + '. ' + item['title'] + '\n')
                i += 1 
                
        except Exception as e:
            print(str(e))
                
        
    elif "bye" or "exit" in query:
        speak("Thanks for having your valuable time with me") 
        speak("I will meet you tomorrow") 
        exit()
        
    
