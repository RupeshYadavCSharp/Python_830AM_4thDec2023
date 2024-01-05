upin=int(input("enter your pin"))

f=open("D:\\pin.txt","r")
fpin=int(f.read())
f.close()

if(upin==fpin):
    f=open("D:\\balance.txt","r")
    bal=int(f.read())
    f.close()
    print("Your balance is ",bal)

    choice=int(input("1.withdraw 2. deposite"))
    if(choice==1):
        amt=int(input("ennter amount to withdraw"))
        bal=bal-amt

        f=open("D:\\balance","w")
        f.write(str(bal))
        f.close()
    else:
        amt=int(input("enter amount to be deposite"))
        bal=bal+amt

        f=open('D:\\balance',"w")
        f.write(str(bal))
        f.close()

else:
    print("invalid pin entered")



