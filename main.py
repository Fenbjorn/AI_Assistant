import datetime
import webbrowser as web
import pywhatkit as pwk
import speech_recognition as sr
import os
import platform
import pyttsx3 as ttx

# Variables de configuration de la voix
engine = ttx.init()
ai_voice = engine.getProperty('rate')
engine.setProperty('rate', 178)
ai_voice = engine.getProperty('voices')
engine.setProperty('voice', ai_voice[0])
ai_name = 'Cobra'


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


# Fonction des commandes
if __name__ == '__main__':
    wish_me()
    command = take_command().lower()
    if 'bonjour' in command:
        print('Bonjour, comment allez-vous ?')
        speak('Bonjour, comment allez-vous ?')

    elif 'au revoir' in command or 'bye' in command or "stop" in command or 'arrête' in command or 'rien' in command:
        print('Au revoir !')
        speak('Au revoir !')

    elif 'google' in command:
        web.open_new_tab('https://www.google.com')
        speak('Ouverture de google')

    elif 'facebook' in command:
        web.open_new_tab('https://www.facebook.com')
        speak('Ouverture de Facebook')

    elif 'youtube' in command:
        web.open_new_tab('https://www.youtube.com')
        speak('Ouverture de Youtube')

    elif 'quelle heure' in command:
        strTime = datetime.datetime.now().strftime("%H:%M")
        speak(f"Il est {strTime}")

    elif 'cherche' in command or 'qu\'est-ce que' in command or 'c\'est quoi' in command or 'recherche' in command:
        command = command.replace('cherche', '')
        command = command.replace('qu\'est-ce que', '')
        command = command.replace('c\'est quoi', '')
        command = command.replace('recherche', '')
        search = f'https://www.google.fr/search?q={command}'
        web.open_new_tab(search)
        speak('Recherche de la demande sur Google')

    elif 'sur Youtube' in command or 'mets du' in command or 'mets la chanson' in command or 'joue' in command:
        command = command.replace('sur Youtube', '')
        command = command.replace('mets du', '')
        command = command.replace('mets la chanson', '')
        command = command.replace('joue', '')
        speak(f'Lecture de {command} sur Youtube')
        pwk.playonyt(command)

    elif 'qui es-tu' in command or 'tu es qui' in command or 'tu peux faire quoi' in command or \
            'tu sais faire quoi' in command or 'que sais-tu faire' in command or 'que peux-tu faire' in command:
        speak(f'Je suis {ai_name}, je suis un assistant virtuel pouvant vous assistez sur certaines tâches simples. '
              'Je peux faire une recherche Google, ouvrir Facebook, Google ou Youtube, jouer de la musique, '
              'vous donner l\'heure. Si vous voulez d\'autres fonctionnalités, veuillez '
              'contacter mon créateur. Merci')

    elif 'qui t\'as fait' in command or 'qui est ton créateur' in command:
        print('Mon créateur se prénomme Fenbjorn, vous pourrez le retrouver sur GitHub')
        speak('Mon créateur se prénomme Fenbjorn, vous pourrez le retrouver sur GitHub')

    elif 'changer ton nom' in command:
        print('Mon nom est Cobra. Mon créateur m\'a donner ce nom car c\'est un type de serpent et parce'
              'qu\'il aime beaucoup la célèbre série d\'animation japonaise diffusé dans les années 80. C\'est '
              'pourquoi je vous demande de ne pas changer mon nom. Merci de votre compréhension.')
        speak('Mon nom est Cobra. Mon créateur m\'a donner ce nom car c\'est un type de serpent et parce'
              'qu\'il aime beaucoup la célèbre série d\'animation japonaise diffusé dans les années 80. C\'est '
              'pourquoi je vous demande de ne pas changer mon nom. Merci de votre compréhension.')


