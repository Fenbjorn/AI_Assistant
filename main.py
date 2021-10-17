import speech_recognition as sr
import pyttsx3 as ttx
import datetime
import wikipedia as wiki
import webbrowser as web
import os
import time
import subprocess as sp
import wolframalpha as wfa
import json
import requests


engine = ttx.init()
ai_voice = engine.getProperty('voices')
engine.setProperty('voice', 'french')


def speak(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print('En écoute...')
        voice = listener.listen(source)
        try:
            command = listener.recognize_google(voice, language='fr-FR')
            print(f'Vous avez dit : {command}\n')
        except Exception as e:
            speak('Désolé, je n\'ai pas compris... Veuillez réessayer')
            return 'None'
        return command


def run_assistant():
    command = take_command()
    if 'Bonjour' in command:
        speak('Bonjour, comment allez-vous ?')


run_assistant()
