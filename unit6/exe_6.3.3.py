import os
from gtts import gTTS
from playsound import playsound

text = "first time I'm using a package in next.py course"

# Create a gTTS object with an indian accent
tts = gTTS(text=text, lang='en', tld='co.in')

audio_file = "output.mp3"
tts.save(audio_file)

playsound(audio_file)

os.remove(audio_file)
