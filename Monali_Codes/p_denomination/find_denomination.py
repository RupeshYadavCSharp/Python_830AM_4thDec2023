amt=int(input("enter any amount:-"))
fh=amt//500
amt=amt%500
th=amt//200
amt=amt%200
h=amt//100
amt=amt%100
f=amt//50
amt=amt%50
t=amt//10
print("denominations of 500 are",fh)
print("denominations of 200 are",th)
print("denominations of 100 are",h)
print("denomination of 50 are",f)
print("denomination of 10 are",t)
