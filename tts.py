import gtts
from playsound import playsound

def play_audio(text):
    tts = gtts.gTTS(text=text, lang='en')
    tts.save("tts.mp3")
    playsound("tts.mp3")
