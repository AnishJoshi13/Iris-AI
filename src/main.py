import os
import pyttsx3
import speech_recognition as sr
import openai
from OpenAI_integration.secrets import MY_API_KEY
from PIL import Image
from matplotlib import pyplot as plt


def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold =  0.6
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"You said: {query}")
            return query
        except Exception as e:
            return "Couldnt get you, can you please repeat"


# Text to Speech
def text_to_speech(phrase):
    engine_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\SPEECH_OneCore\Voices\Tokens\MSTTS_V110_enUS_ZiraM'
    engine = pyttsx3.init()
    engine.setProperty('voice', engine_id)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(phrase)
    engine.runAndWait()
    # engine = pyttsx3.init()
    # engine.say(phrase)
    # engine.runAndWait()


if __name__ == '__main__':
    openai.api_key = MY_API_KEY
    current_dir = os.getcwd()
    image_file = 'IrisLogo.png'
    image_path = os.path.join(current_dir, image_file)
    image = Image.open(image_path)
    plt.imshow(image)
    plt.axis('off')
    plt.show()

    while 1:
        prompt = speech_to_text()
        if "Iris" in prompt:
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=prompt,
                temperature=0.7,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )
            generated_text = response["choices"][0]["text"]
            text_to_speech(generated_text)
