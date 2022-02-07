import speech_recognition as s_r
print ("List of microphones:")
print(s_r.Microphone.list_microphone_names()) #print all the microphones connected to your machine