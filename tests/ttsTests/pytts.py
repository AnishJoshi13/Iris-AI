# import pyttsx3
# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)
# engine.say('The quick brown fox jumped over the lazy dog.')
# engine.runAndWait()

import pyttsx3
import time

def play_phrase(phrase, engine_id):
    engine = pyttsx3.init()
    engine.setProperty('voice', engine_id)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(phrase)
    engine.runAndWait()

def main():
    engine_ids = ['HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\SPEECH_OneCore\Voices\Tokens\MSTTS_V110_enUS_ZiraM',  # Example engine IDs for Windows
                  'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\SPEECH_OneCore\Voices\Tokens\MSTTS_V110_enUS_ZiraPro']

    for engine_id in engine_ids:
        print(f"Playing with engine: {engine_id}")
        phrase = "Sure! It seems like you're in need of some water. Hydration is important for your well-being. Take a moment to refresh yourself and drink some water. Stay hydrated!"
        play_phrase(phrase, engine_id)
        time.sleep(3)  # Wait for 3 seconds before playing with the next engine

if __name__ == '__main__':
    main()
