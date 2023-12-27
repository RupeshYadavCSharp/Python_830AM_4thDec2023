sal=float(input("enter salary\n"))
if(sal>=1 and sal<=150000):
    tax1=0
    print("tax is",tax1)
elif(sal>=150000 and sal<=300000):
    tax2=10/100*sal
    print("tax is",tax2)
elif(sal>=300000 and sal<=500000):
    tax3=20/100*sal
    print("tax is",tax3)
elif(sal>=500000 ):
    tax4=30/100*sal
    print("tax is",tax4)