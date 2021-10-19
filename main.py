import datetime
import webbrowser as web
import pywhatkit as pwk
import functions as f

# Corps principal du code
if __name__ == '__main__':
    f.wish_me()
    while True:
        command = f.take_command().lower()
        if 'bonjour' in command:
            print('Bonjour, comment allez-vous ?')
            f.speak('Bonjour, comment allez-vous ?')
            break
        elif 'au revoir' in command or 'bye' in command or "stop" in command or 'arrête' in command:
            print('Au revoir !')
            f.speak('Au revoir !')
            break
        elif 'google' in command:
            web.open_new_tab('https://www.google.com')
            f.speak('Ouverture de google')
            break
        elif 'facebook' in command:
            web.open_new_tab('https://www.facebook.com')
            f.speak('Ouverture de Facebook')
            break
        elif 'youtube' in command:
            web.open_new_tab('https://www.youtube.com')
            f.speak('Ouverture de Youtube')
            break
        elif 'quelle heure' in command:
            strTime = datetime.datetime.now().strftime("%H:%M")
            f.speak(f"Il est {strTime}")
            break
        elif 'cherche' in command:
            command = command.replace('cherche', '')
            search = f'https://www.google.fr/search?q={command}'
            web.open_new_tab(search)
            f.speak('Recherche de la demande sur Google')
            break
        elif 'recherche' in command:
            command = command.replace('recherche', '')
            search = f'https://www.google.fr/search?q={command}'
            web.open_new_tab(search)
            f.speak('Recherche de la demande sur Google')
            break
        elif 'c\'est quoi' in command:
            command = command.replace('c\'est quoi', '')
            search = f'https://www.google.fr/search?q={command}'
            web.open_new_tab(search)
            f.speak('Recherche de la demande sur Google')
            break
        elif 'qu\'est-ce que' in command:
            command = command.replace('qu\'est-ce que', '')
            search = f'https://www.google.fr/search?q={command}'
            web.open_new_tab(search)
            f.speak('Recherche de la demande sur Google')
            break
        elif 'joue' in command:
            command = command.replace('joue', '')
            f.speak(f'Lecture de {command} sur Youtube')
            pwk.playonyt(command)
            break
        elif 'mets la chanson' in command:
            command = command.replace('mets la chanson', '')
            f.speak(f'Lecture de {command} sur Youtube')
            pwk.playonyt(command)
            break
        elif 'mets du' in command:
            command = command.replace('mets du', '')
            f.speak(f'Lecture de {command} sur Youtube')
            pwk.playonyt(command)
            break
        elif 'sur Youtube' in command:
            command = command.replace('sur Youtube', '')
            f.speak(f'Lecture de {command} sur Youtube')
            pwk.playonyt(command)
            break
        elif 'qui es-tu' in command or 'tu es qui' in command or 'tu peux faire quoi' in command or \
                'tu sais faire quoi' in command or 'que sais-tu faire' in command or 'que peux-tu faire' in command:
            f.speak('Je suis PY-AI, je suis un assistant virtuel pouvant vous assistez sur certaines tâches simples. '
                    'Je peux faire une recherche Youtube ou Google, ouvrir Facebook, vous donner '
                    'l\'heure. Si vous voulez d\'autres fonctionnalités, veuillez '
                    'contacter mon créateur. Merci')
            break
        elif 'qui t\'as fait' in command or 'qui est ton créateur' in command:
            print('Mon créateur se prénomme Fenbjorn, vous pourrez le retrouver sur GitHub')
            f.speak('Mon créateur se prénomme Fenbjorn, vous pourrez le retrouver sur GitHub')
            break

