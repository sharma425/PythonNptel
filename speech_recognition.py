import speech_recognition as sr

audio_file=("male600.wav")
r=sr.Recognizer()
with sr.AudioFile(audio_file) as source:
    audio = r.record(source)
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