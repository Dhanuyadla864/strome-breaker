import speech_recognition as SR

import pyttsx3

import wikipedia

def speak(text):
    a = pyttsx3.init()

    a.say()

    a.runAndWait()

def input():


    b = SR.Recognizer()

    with SR.Microphone() as s:

        print("start speaking..... ")

        audio = b.listen(s)

        c = b.recognize_google(audio)

        return c

def output():
    
    c = input().lower()

    print("we spoke:{c}")

    d = wikipedia.summary(C,sentences=3)

    print(d)

    speak("wikipedia said:")

    speak(d)

    speak("Hello Dhanu i'm Strome Breaker i'm your personal assistant")

    speak("what can i do for you")

    output()




