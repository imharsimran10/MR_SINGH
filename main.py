import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import smtplib
import pyjokes
from News import *
from YT import music
from selenium_webdriver import infow

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 200)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning !")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good evening")

    speak("I am Mr. Singh Sir, your Right Arm. Hope you are having a great day.")
    text1 = takeCommand()
    if "what" and "about" and "you" in text1:
        speak("I am also having a Good Day Sir.")
    speak("How may I help you Sir?")


def takeCommand():
    # it takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        print("Listening ...")
        r.energy_threshold = 10000
        #r.pause_threshold = 1  # consider the 1 second non audio silence to consider the sentence complete
        # r.energy_threshold=250
        r.adjust_for_ambient_noise(source, 1.2)

    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}\n")
    except Exception as e:
        print(e)
        print("Say that again please ...")
        return "none"
    return query


def sendemail(to, content):
    server = smtplib.SMTP('smntp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("youremail.com", "your pass")
    server.sendmail('your email', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        # logic for executing tasks based on query
        if 'Search' and 'wikipedia' in query:
            speak(" Search about what Sir ?")
            content = takeCommand()
            speak('Searching for {} in wikipedia Sir...'.format(content))
            assist = infow()
            assist.get_info(content)
           # results = wikipedia.summary(query, sentences=2)
            #speak('According to wikipedia')
            #print(results)
            #speak(results)

        elif "news" in query:
            print("Sure Sir, Now I will read news for you.")
            speak("Sure Sir, Now I will read news for you.")
            arr= news()
            for i in range(len(arr)):
                print(arr[i])
                speak(arr[i])

        elif 'wish me' in query:
            wishMe()
        elif 'joke' in query:
            result = pyjokes.get_joke(language='en', category='all')
            print(result)
            speak(result)
        elif "youtube" in query:
            speak('Which Video Sir ?')
            vid = takeCommand().lower()
            print("Playing {} on youtube sir".format(vid))
            speak("Playing {} on youtube sir".format(vid))
            assist = music()
            assist.play(vid)

        elif "open google" in query:
            wb.open("google.com")
        elif 'open stackoverflow' in query:
            wb.open("stackoverflow.com")
        # elif 'play music ' in query:
        # mu_dir= dir daldo alpi mein se
        # songs=os.listdir(mu_dir)
        # print(songs)
        # os.startfile(os.path.join(music_dir,songs[0]))we can also import rand module and play random  moduLE

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir , the time {strTime}")
        elif 'open code' in query:
            codepath = "C:\\Users\\js290\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
            os.startfile(codepath)
        elif 'send email to ikjyot' in query:
            try:
                speak("What should i write")
                content = takeCommand()
                to = "ikjyot150@gmail.com"
                sendemail(to, content)
                speak("Email has been sent!")
            except  Exception as e:
                print(e)
                speak("Sorry, I am ynable to send the email")
        elif 'exit' in query:
            speak("happy to serve you Sir")
            exit()
