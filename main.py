# Smart Desktop Voice Assistant

import pyttsx3
import datetime
import smtplib
import wikipedia
import speech_recognition as sr
import webbrowser
import os

# sapi5 is voice api by Microsoft 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    # Great as per current time
    hour=int(datetime.datetime.now().hour) 
    if hour>=0 and hour <12:
        speak("Good Morning")
    elif hour>12 and hour <18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("Hi User ! I am your Smart Desktop voice Assistant!Please tell me how can i help you?")

def takeCommand():
    # Take mic input from user and op as string
    r=sr.Recognizer()
    with  sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing.....")
        query=r.recognize_google(audio,language="en-in")
        print(f"User said : {query}\n")
    except Exception as e:
        print(e)  #prints error
        print("Say that again Please...")
        return "None"
    return query 

#must allow Less secure app on your email account to send the email
def sendEmail(to,content):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("your email","pwd")
    server.sendmail("your email",to,content)
    server.close()

if __name__ == "__main__":
    wishme()
    while True:
        query=takeCommand().lower()

        #tasks 
        if "wikipedia" in query:
            speak("Searching Wiki.....")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("Acccording to wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")
        
        elif "play music" in query:
            music_dir="" #path of music folder
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        
        elif "time" in query:
            now = datetime.datetime.now()
            t = now.strftime("%H:%M:%S")
            speak(f"Sir the time is {t}")

        elif "open code" in query:
            print("Opening Vs Code")
            path=r"" #path of exe application
            os.startfile(path)


        elif "email" in query:
            try:
                speak("What shuld I say ?")
                content=takeCommand()
                to="reciver email"
                sendEmail(to,content)
                speak("Email send")
            except Exception as e:
                print(e)
                speak("Sorry unable to send currently")

        elif "quit" in query:
            speak("Goodbye user !see you Soon")
            exit()
