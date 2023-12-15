num=int(input("enter 4 digit number:-"))
a=num%10  #last
b=num//1000  #1st
c=num%100
d=c//10  #3rd
e=num//100
f=e%10  #2nd

print(a,d,f,b)

