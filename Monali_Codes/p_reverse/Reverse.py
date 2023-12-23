# num=int(input("enter any 3 digit no:"))
# a=num%10  #last no.
# b=num//100 #1st no.
# c=num//10  #1st 2 no.
# d=c%10   #mid no.
# print(a,d,b)

numm=int(input("enter any 4 digit no:-"))
a1=numm%100
b1=a1//10 #3rd no.
c1=numm//100
d1=c1%10  #2nd no.
e=numm//1000 #1st no
f=numm%10 #last no.
print(e,b1,d1,f)



