import speech_recognition as sr
import pyttsx3

# Speech to Text
def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak something...")
        audio = recognizer.listen(source, timeout=2)

    try:
        text = recognizer.recognize_google(audio)
        print("You said :",text)
        return text
    except sr.UnknownValueError:
        print("Unable to recognize speech")
    except sr.RequestError as e:
        print("Error occurred; {0}".format(e))

# Text to Speech
def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == '__main__':
    while 1:
        output_text = speech_to_text()
        text_to_speech(output_text)
