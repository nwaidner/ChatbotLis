import gtts
from playsound import playsound
from config import AUDIO_PATH


def play_audio(text):
    tts = gtts.gTTS(text=text, lang='en')
    tts.save(AUDIO_PATH)
    playsound(AUDIO_PATH)
