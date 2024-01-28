# def area(l,b):
#     a=l*b
#     print("The area of rectangle is",a)
# def main():
#     l=int(input("enter l="))
#     b=int(input("enter b="))
#     area(l,b)
# main()
#
#
# def sum(a,b,c):
#     d=(a+b)/c
#     return d
# def main():
#     a=int(input("enter a"))
#     b=int(input("enter b"))
#     c=int(input("enter c"))
#     d=sum(a,b,c)
#     print("The calculation is",d)
# main()
#
#
# def getTax(sal):
#     if(sal>=500000):
#         tax=sal/10
#         print("The tax on salary is",tax)
#     else:
#         print("There is zero tax on salary")
#
# def main():
#     sal=float(input("enter salart="))
#     getTax(sal)
# main()
#
#
# def getFullName(fname,mname,lname):
#     name=fname+mname+lname
#     return name
# def main():
#     fname=input("enter fname ")
#     mname=input("enter middle name ")
#     lname=input("enter last name")
#     name=getFullName(fname ,mname ,lname)
#     print("Full name is",name)
# main()
#
# def isEven(num)->bool:
#     if(num%2==0):
#         print("Its an even number")
#     else:
#         print("Its an odd number")
# def main():
#     num=int(input("enter number="))
#     isEven(num)
# main()
#
#
#
# for i in range(1,6):
#     for j in range(i):
#         print("*",end=" ")
#     print()
# print()
#
# for i in range(1,6):
#     for j in range(6-i):
#         print("*",end=" ")
#     print()
# print()
# for i in range(1,6):
#     for j in range(1,10):
#         if(j>=6-i and j<=4+i):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


num=int(input("enter any number="))
large=0
while(num!=0):
    rem=num%10
    if(rem>large):
        large=rem
    num=num//10
print("The largest number is",large)

num=int(input("enter any number="))
small=9
while(num!=0):
    rem=num%10
    if(rem<small):
        small=rem
    num=num//10
print("The smallest no is",small)


num=int(input("enter any number:="))
count=0
while(num!=0):
    num=num//10
    count+=1


print("The number of digit entered is",count)
