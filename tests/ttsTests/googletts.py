from gtts import gTTS
import os

text = "Iris, at your Service Sir"

# Create a text-to-speech object
tts = gTTS(text=text, lang='en')

# Save the speech as an audio file
tts.save('output.mp3')

# Play the audio file
os.system('output.mp3')
