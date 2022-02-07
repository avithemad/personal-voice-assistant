import speech_recognition as s_r
import time

print(s_r.__version__)  # just to print the version not required
r = s_r.Recognizer()
my_mic = s_r.Microphone(
    device_index=1
)  # my device index is 1, you have to put your device index

with my_mic as source:
    c = time.time()
    print("Say now!!!!")
    audio = r.listen(source)  # take voice input from the microphone
    print(time.time() - c)
print(r.recognize_google(audio))  # to print voice into text
