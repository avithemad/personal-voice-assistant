from gtts import gTTS
from playsound import playsound

tts = gTTS("hello avinash jayakar", lang="en", tld="co.uk")
tts.save("test.mp3")
playsound("test.mp3")
