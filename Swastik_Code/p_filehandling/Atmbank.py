import datetime
from fpdf import FPDF
import pyttsx3

upin=int(input("enter pin"))
f=open("D:\\pin.txt","r")
fpin=int(f.read())
f.close()
if(upin==fpin):
    f=open("D:\\balance.txt","r")
    bal=int(f.read())
    f.close()
    print("current balance is ",bal)
    choice=int(input("1.withdraw 2.deposit 3.changepin 4.show statement 5.print statement 6.read statement"))
    if(choice==1):
        amt=int(input("enter amount to be withdraw"))
        bal=bal-amt
        f=open("D:\\balance.txt","w")
        f.write(str(bal))
        f.close()
        msg="withdraw money of "+ str(amt)+"on"+str(datetime.datetime.now())+"\n"
        f=open("D:\\log.txt","a")
        f.write(msg)
        f.close()
    elif(choice==2):
        amt=int(input("enter amount to deposit"))
        bal=bal+amt
        f=open("D:\\balance.txt","w")
        f.write(str(bal))
        f.close()
        msg="deposit of money of " + str(amt) + "on" + str(datetime.datetime.now()) + "\n"
        f=open("D:\\log.txt","a")
        f.write(msg)
        f.close()
    elif(choice==3):
        npin=int(input("enter new pin"))
        f=open("D:\\pin.txt","w")
        f.write(str(npin))
        f.close()
        msg="pin is changed by user on " + str(datetime.datetime.now()) + "\n"
        f=open("D:\\log.txt","a")
        f.write(msg)
        f.close()
    elif(choice==4):
        f=open("D:\\log.txt","r")
        log=f.read()
        print(log)
        f.close()
    elif(choice==5):
        f=open("D:\\log.txt","r")
        log=f.read()
        f.close()
        obj=FPDF()
        obj.add_page()
        obj.set_font("Arial",size=15)
        obj.write(5,log)
        obj.output("D:\\log.pdf")
    elif(choice==6):
        f=open("D:\\balance.txt","r")
        bal=f.read()
        f.close()
        obj=pyttsx3.init()
        voices = obj.getProperty("voices")
        obj.setProperty("voice", voices[1].id)
        text=bal
        obj.say(text)
        obj.runAndWait()
else:
    print("invalid pin")
    msg="invalid pin was entered on " + str(datetime.datetime.now()) + "\n"
    f=open("D:\\log.txt","a")
    f.write(msg)
    f.close()