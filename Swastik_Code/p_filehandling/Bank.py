ff=open("D:\\pin.txt","w")
pin=input("enter pin")
print(pin)
ff.write(pin)
ff.close()

sf=open("D:\\balance.txt","a")
bal=input("enter bal")
print(bal)
sf.write(bal)
sf.close()

print("enter your pin")
if(pin==1234):
    print("your balace is ",bal)
    a=withdraw
    b=deposit
    print("choose one")
elif(pin!=1234):
    print("your pin is invalid")
