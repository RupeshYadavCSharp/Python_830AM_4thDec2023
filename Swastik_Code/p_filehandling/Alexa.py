import speech_recognition
import pyaudio
from google.cloud import texttospeech
import webbrowser
import distutils

recognizer = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print("Listening...")
    audio = recognizer.listen(source)

text = recognizer.recognize_google(audio)
print("You said: ", text)
try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")
query=text
for j in search(query,tld="co.in",num=1,stop=1,pause=1):
    print(j)