upin=int(input("enter pin"))
f=open("D:\\pin.txt","r")
fpin=int(f.read())
f.close()
if(upin==fpin):
    f=open("D:\\balance.txt","r")
    bal=int(f.read())
    f.close()
    print("current balance is",bal)
    choice=int(input("1.withdraw 2.deposit 3.changepin"))
    if(choice==1):
        amt=int(input("enter amount to be withdraw"))
        bal=bal-amt
        f=open("D:\\balance.txt","w")
        f.write(str(bal))
        f.close()
    elif(choice==2):
        amt=int(input("enter amount to deposit"))
        bal=bal+amt
        f=open("D:\\balance.txt","w")
        f.write(str(bal))
        f.close()
    elif(choice==3):
        npin=int(input("enter new pin"))
        f=open("D:\\pin.txt","w")
        f.write(str(npin))
        f.close()
else:
    print("invalid pin")