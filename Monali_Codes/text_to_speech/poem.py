import pyttsx3
engine=pyttsx3.init()
#
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
#
# p=open("D:\\poem.txt","r")
# s=p.read()
# p.close()
#
# engine.say(s)
# engine.runAndWait()

# s=open("D:\\song.txt","r")
# a=s.read()
# s.close()
#
# engine.say(a)
# engine.runAndWait()





