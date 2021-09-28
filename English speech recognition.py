import speech_recognition as sr
import os
os.chdir("C:/Users/User/Desktop/master")
r=sr.Recognizer()
havard = sr.AudioFile("gg.wav")
with havard as source:
    audio= r.record(source)
r.recognize_google(audio)
