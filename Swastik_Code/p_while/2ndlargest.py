num=int(input("enter any number"))
small=9
while(num!=0):
    rem=num%10
    if(rem<small):
        small=rem
    num=num//10
print(small)