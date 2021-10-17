import speech_recognition as sr
import os
import platform
import pyttsx3 as ttx
import datetime

# Variables de configuration de la voix
engine = ttx.init()
ai_voice = engine.getProperty('voices')
engine.setProperty('voice', ai_voice[0])


# Fonction qui récupère l'os et retourne le nom de l'utilisateur en fonction de l'os
def os_name():
    # Variable permettant de récupérer l'os
    osname = platform.system()

    if osname == 'Windows':
        user = os.getenv('username')
    else:
        user = os.environ['USER']
    return user


# Fonction qui donne la parole à l'ia
def speak(text):
    engine.say(text)
    engine.runAndWait()


# Fonction qui récupère votre commande vocale
def take_command():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print('Que puis-je pour vous ?')
        speak('Que puis-je pour vous ?')
        voice = listener.listen(source)
        try:
            command = listener.recognize_google(voice, language='fr-FR')
            print(f'Vous avez dit : {command}\n')
        except Exception as e:
            speak('Désolé, je n\'ai pas compris... Veuillez réessayer')
            return 'None'
        return command


# Fonction qui souhaite la bienvenue en fonction de l'heure
def wish_me():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 18:
        print(f'Bonjour {os_name()}')
        speak(f'Bonjour {os_name()}')
    else:
        print(f'Bonsoir {os_name()}')
        speak(f'Bonsoir {os_name()}')

