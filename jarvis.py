import contextlib
import pyttsx3 
import SpeechRecognition as sr
import datetime
import wikipedia        
import webbrowser
import os
import smtplib

Engine = pyttsx3.init('sapi5')
voices = Engine.getPorperty('voices')
print(voices[0].id)
Engine.setProperty('voices', voices[0].id )
    
def speak(audio):
    Engine.say(audio)
    Engine.runAndWait()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
        
    elif hour>=12 and hour<18:
        speak("Good Afternoon") 
        
    else:
        speak("Good Evening")
    
    speak("I am jarvis Sir. please tell me how may I help you")           
        
        
def takeCommand():
    #It take microphone input from the user and return string output
    
    r = sr.Recognition()
    with sr.Microphone() as source:
        print("Listerning...")
        r.pause_thresold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r. recognize_google(audio, Language='en-in')
        print(f"User Said: {query}\n")
        
    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"    
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com','your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()
    
if __name__ == "__main__":
    wishMe()
    
    while True:
        query = takeCommand().lower()
        
        
        #Logic for executing task based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=1)
            speak("According to wikipedia")
            print(results)
            speak(results)
            
            
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            
        elif 'open google' in query:
            webbrowser.open("google.com")
            
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
            
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            
        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
            
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            
        elif 'open code' in query:
            codePath = "C:\\Users\\user\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            
        elif 'email to ekansh' in query:
            try:
                speak("what sholud I say?")
                context = takeCommand() 
                to = "ekanshdevlekar20@gmail.com"
                sendEmail(to, context)
                speak("Email has be sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to share the Email")
                
                
            