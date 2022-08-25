from gtts import gTTS
from playsound import playsound

audio ='speech.mp3'
language = 'es'
sp = gTTS(text = "probando python en mi computadora, esto está vacilón", lang = language, slow = False)

sp.save(audio)
playsound(audio)