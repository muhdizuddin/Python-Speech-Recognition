import speech_recognition as sr
import os
os.chdir("Your voice directory")
r=sr.Recognizer()
havard = sr.AudioFile("Your voice in wav file")
with havard as source:
    audio= r.record(source)
r.recognize_google(audio)
