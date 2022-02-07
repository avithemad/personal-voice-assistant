from operator import contains
import webbrowser
import speech_recognition as sr

from gtts import gTTS
from playsound import playsound
import keyboard  # using module keyboard

import winsound


# Sample rate is how often values are recorded
sample_rate = 48000
# Chunk is like a buffer. It stores 2048 samples (bytes of data)
# here.
# it is advisable to use powers of 2 such as 1024 or 2048
chunk_size = 2048
# Initialize the recognizer
r = sr.Recognizer()

open_pipeline = ["open", "pipe", "line"]

open_code = ["open", "code"]

while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed("ctrl+c"):
            exit()
        if keyboard.is_pressed("f8"):  # if key 'q' is pressed
            with sr.Microphone(
                device_index=1, sample_rate=sample_rate, chunk_size=chunk_size
            ) as source:
                winsound.Beep(200, 100)
                # wait for a second to let the recognizer adjust the
                # energy threshold based on the surrounding noise level
                r.adjust_for_ambient_noise(source)
                print("Say Something")
                # listens for the user's input
                audio = r.listen(source)

                try:
                    text = r.recognize_google(audio)
                    print("you said: " + text)
                    if all(c in text for c in open_pipeline):
                        webbrowser.open(
                            "https://dev.azure.com/itron/SoftwareProducts/_build"
                        )
                    if all(c in text for c in open_code):
                        webbrowser.open(
                            "https://dev.azure.com/itron/SoftwareProducts/_git/"
                        )
                    if "quit" in text:
                        exit()

                    winsound.Beep(300, 100)

                # error occurs when google could not understand what was said

                except sr.UnknownValueError:
                    print("Google Speech Recognition could not understand audio")
                    winsound.Beep(500, 100)

                except sr.RequestError as e:
                    print(
                        "Could not request results from GoogleSpeech Recognition service; {0}".format(
                            e
                        )
                    )
                    winsound.Beep(500, 100)
    except:
        break  # if user pressed a key other than the given key the loop will break
