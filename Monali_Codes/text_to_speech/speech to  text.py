import speech_recognition

recognizer=speech_recognition.Recognizer()

with speech_recognition.Microphone() as source:
    print("Listening........")
    audio=recognizer.listen(source)



text=recognizer.recognize_google(audio)
print("you said ",text)

