import os
import pyttsx3
from PIL import Image
from matplotlib import pyplot as plt


# Text to Speech
def text_to_speech(phrase):
    engine_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\SPEECH_OneCore\Voices\Tokens\MSTTS_V110_enUS_ZiraM'
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')  # Get the current speech rate
    engine.setProperty('rate', rate - 20)
    engine.setProperty('voice', engine_id)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(phrase)
    engine.runAndWait()


if __name__ == '__main__':
    phrase = "Oh, absolutely! Because getting some water is the most groundbreaking and life-changing task one could ever undertake. I mean, who needs oxygen, right? It's not like our bodies are mostly made up of water or anything. So, please, by all means, drop everything you're doing and go get that incredibly vital glass of water. Your existence depends on it!"
    text_to_speech(phrase)
    # Get the current working directory
    current_dir = os.getcwd()

    # Specify the relative path to the image file from the current directory
    image_file = 'IrisLogo.png'

    # Construct the full path to the image file
    image_path = os.path.join(current_dir, image_file)

    # Open the image file
    image = Image.open(image_path)

    # Display the image
    plt.imshow(image)
    plt.axis('off')  # Optional: turn off axes
    plt.show()
