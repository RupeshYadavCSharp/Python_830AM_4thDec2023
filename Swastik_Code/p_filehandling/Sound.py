import pyttsx3

f=open("D:\\poem.txt","r")
poem=f.read()
f.close()
engine=pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)
text=poem
engine.say(text)
engine.runAndWait()