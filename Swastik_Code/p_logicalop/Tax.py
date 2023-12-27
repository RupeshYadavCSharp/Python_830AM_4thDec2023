#code for finding tax in income
sal=float(input("enter salary\n"))        #enter salary 100000
if(sal>=1 and sal<=150000):               #100000<150000(condition true)
    tax1=0                                #tax = 0
    print("tax is",tax1)                  #tax is 0
elif(sal>=150000 and sal<=300000):
    tax2=10/100*sal
    print("tax is",tax2)
elif(sal>=300000 and sal<=500000):
    tax3=20/100*sal
    print("tax is",tax3)
elif(sal>=500000 ):
    tax4=30/100*sal
    print("tax is",tax4)