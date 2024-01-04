import pyttsx3

f=open("D:\\poem.txt","r")
poem=f.read()
f.close()
file=pyttsx3.init()
voices = file.getProperty("voices")
file.setProperty("voice",voices[1].id)
text=poem
file.say(text)
file.runAndWait()