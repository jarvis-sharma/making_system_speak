import pyttsx3
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty(voices, voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('good morning')
    elif hour >= 12 and hour <= 16:
        speak('good afternoon')
    else:
        speak('good evening')
    speak("I'm Jarvis, how may i help you?")


def takecommand():
    s = input()
    speak(s)


wishme()
takecommand()
