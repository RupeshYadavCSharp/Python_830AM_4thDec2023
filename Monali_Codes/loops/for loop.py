# # for i in range(1,11,1):
# #     print(i,end=",")
# #
# # for i in range(2,21,2):
# #     print(i,end=" ")
#
# # for i in range(10,0,-1):
# #     print(i,end=" ")
#
# # num=int(input("enter any number:"))
# # for i in range(1,num+1):
# #      print(i,end=" ")
#
# # num=int(input("enter any number:"))
# #
# # sum=0
# # for i in range(1,num+1):
# #  sum=sum+i
# #  print("The sum is",sum)
#
# #
# # num=int(input("enter any number"))
# # sum=0
# #
# # for i in range(1,num+1):
# #  sum=sum+'i
# #  print(sum)
#
# #
# # for i in range(1,11):
# #     print(i,end=" ")
# #     if(i<10):
# #         print(",",end=" ")
# #     else:
# #         print(".",end=" ")
#
#
# # Factorial
#
# # num=int(input("enter any number:-"))
# # result=1
# #
# # for i in range(1,num+1):
# #     result=i*result
# #
# # print("Factorial of ",num, "is",result)
#
# # pencils
# # num=int(input("enter any number:-"))
# # a=0
# # for i in range(1,num+1):
# #     a=i**2+a
# #
# # print("number of pencils got in", num,"std is", a)
#
# # fibbonacii number series:
# count=int(input("Enter Count"))
#
# f=0
# s=1
# print(f," ",s,end=" ")
# for i in range(1,count-1):
#     t=f+s
#     print(t,end=" ")
#
#     f=s
#     s=t
# for i in range(10,0,-1):
#     print(i,end=" ")

# num=int(input('enter any number='))
# for i in range(1,num+1):
#     print(i,end=" ")

#
# num=int(input("enter any number="))
# a=0
# for i in range(1,num+1):
#     a=i**2+a
# print("pencils receive in class",num,"is",a)


# cls=int(input("enter any class="))
# a=0
# for i in range(1,cls+1):
#     a=i**2+a
# print("pencils receive in class",cls,"is",a)


# num=int(input("enter any number="))
# # flag=True
# # for i in range(2,num):
# #     if(num%i==0):
# #         flag=False
#
# if(flag==True):
#     print("its a prime number")
# else:
#     print('its not a prime number')
#
#
# for i in range(10,0,-1):
#     print(i,end=" ")
#

for i in range(1,6):
    for j in range(i):
        print("*",end=" ")
    print()

print()

for i in range(1,6):
    for j in range(1,6):
        print("*",end=" ")
    print()
print()





for i in range(1,6):
    for j in range(6-i):
        print("*",end=" ")
    print()
print()

for i in range(1,6):
    for j in range(1,10):
        if(j>=6-i and j<=4+i):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print()

for i in range(1,6):
    for j in range(1,10):
        if(j>=6-i and j<=4+i):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print()

for i in range(1,6):
   for j in range(1,10):
     if(j>+6-i and j<=4+i):
        print("*",end=" ")
     else:
        print(" ",end=" ")
   print()

