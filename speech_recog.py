import speech_recognition as sr
import os

audio_file=("Notepad command.wav")
r=sr.Recognizer()      #initialize the recognizer
with sr.AudioFile(audio_file) as source:
    audio = r.record(source)        #read the audio file
    try:
        # using google speech recognition
        text = r.recognize_google(audio)
        print('Converting audio transcripts into text ...')
        print("audio file contains : \n" + text)
    except sr.UnknownValueError :
        print("Google speech recognition could not understand audio")
    except sr.RequestError :
        print("couldn't get the result from google speech recognition")
    except:
        print('Sorry.. run again...')
