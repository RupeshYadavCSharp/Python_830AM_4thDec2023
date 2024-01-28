# for i in range(1,6):
#     for j in range(i):
#         print("*",end=" ")
#     print()
#
#
# print()
#
# for i in range(1,6):
#     for j in range(6-i):
#         print("*",end=" ")
#     print()
#
# print()
#
# for i in range(1,6):
#     for j in range(1,10):
#         if(j>=6-i and j<=4+i):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#
# for i in range(1,6):
#     for j in range(1,10):
#         if(j>=6-i and j<=4+i):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#
# for i in range(1,6):
#     for j in range(1,10):
#         if(j>=6-i and j<=4+i):
#             print("*",end=" ")
#
#         else:
#             print(" ",end=" ")
#     print()
#
# for i in range(1,6):
#     for j in range(1,10):
#         if(j>=6-i and j<4+i):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# num=int(input("enter any number:="))
# flag=True
# for i in range(2,num):
#     if(num%i==0):
#         flag=False
# if(flag==True):
#     print("its prime number")
# else:
#     print("its not a prime number")


# find the num of the digits in loop?

# num=int(input("enter any number:="))
# sum=0
# while(num!=0):
#     rem=num%10
#     sum=sum+rem
#     num=num//10
# print("The sum is",sum)

#
# num=int(input("enter any number"))
# sum=0
# while(num!=0):
#     rem=num%10
#     sum=sum+rem
#     num=num//10
# print("The sum of entered digit is",sum)


# num=int(input("enter any number="))
# count=0
# while(num!=0):
#     num=num//10
#     count=count+1
# print("you have entered",count,"digit number")


# num=int(input("enter any number:-"))
# small=9
# while(num!=0):
#     rem=num%10
#     if(rem<small):
#         small=rem
#     num=num//10
# print("The smallest number is",small)


# programme to print the number of digit entered

# num=int(input("enter any number="))
# small=9
# while(num!=0):
#     rem=num%10
#     if(rem<small):
#         small=rem
#     num=num//10
# print("The smallest digit is",small)
#
#
# for i in range(10,0,-1):
#     print(i,end=" ")
#
#
# list=[166,687,89,989,457]
# for i in list:
#     print(i)
#
# list1=[12,789,45,89899,45]
# for i in list1:
#     print(i)
#
# n=int(input("enter any number:-"))
# sum=0
# for i in range(1,n+1):
#       sum=sum+i
# print("The sum of all is",sum)
#
# n=int(input("enter any number="))
# sum=0
# for i in range(1,n+1):
#     sum=sum+i
# print("The sum of all is",sum)


# for i in range(1,6):
#     for j in range(1,10):
#         if(j>=6-i and j<=4+i):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#
# for i in range(1,6):
#     for j in range(i):
#         print("*",end=" ")
#     print()
#
# for i in range(1,6):
#     for j in range(6-i):
#         print("*",end=" ")
#     print()

# num=int(input("enter any number:-"))
# flag=True
# for i in range(2,num):
#     if(num%i==0):
#         flag=False
#
#
# if(flag==True):
#     print("its a prime number")
# else:
#     print("its not a prime number")


# # Get input from the user
# try:
#     number = int(input("Enter a number to calculate its factorial: "))
#     if number < 0:
#         print("Factorial is not defined for negative numbers.")
#     else:
#         result = 1
#         for i in range(2, number + 1):
#             result *= i
#         print(f"The factorial of {number} is: {result}")
#
#
# num=int(input("enter any number="))
# if(num<o):
#     print("enter positive number")
# else:
#     result=1
#     for i in range(2,num+1):
#         result=i*result
#     print("Factorial of",num, "is",result)
#
# except ValueError:
#     print("Invalid input. Please enter a valid integer.")


# # Get input from the user
# try:
#     number = int(input("Enter a number to calculate its factorial: "))
#     if number < 0:
#         print("Factorial is not defined for negative numbers.")
#     else:
#         result = 1
#         for i in range(2, number + 1):
#             result *= i
#         print(f"The factorial of {number} is: {result}")
# except ValueError:
#     print("Invalid input. Please enter a valid integer.")


# # Get input from the user
# try:
#     number = int(input("Enter a number to calculate its factorial: "))
#     if number < 0:
#         print("Factorial is not defined for negative numbers.")
#     else:
#         result = 1
#         for i in range(2, number + 1):
#             result *= i
#         print(f"The factorial of {number} is: {result}")
# except ValueError:
#     print("Invalid input. Please enter a valid integer.")

# def add():
#     n1=int(input("enter n1"))
#     n2=int(input("enter n2"))
#     n3=n1+n2
#     print("The sum is",n3)
# def sub():
#     n1=int(input("enter n1"))
#     n2=int(input("enter n2"))
#     n3=n1-n2
#     print("The subtraction is",n3)
# def main():
#     num=int(input("1.sum\n2.subtraction\n"))
#     if(num==1):
#         add()
#     elif(num==2):
#         sub()
# main()

# def area(l,b)->int:
#     a=l*b
#     return a
# def main():
#     l=int(input("enter lenght="))
#     b=int(input("enter breath="))
#     a=area(l,b)
#     print("The area of rectangle is ",a)
# main()



# def add(n1,n2):
#     c=n1+n2
#     return c
# def main():
#     n1=int(input("Enter n1"))
#     n2=int(input("enter n2"))
#     c=add(n1,n2)
#     print("The addition is",c)
# main()


# def area(l,b):
#     a=l*b
#     print("The area of rectangle is",a)
# def main():
#     l=int(input("enter l"))
#     b=int(input("enter b"))
#     area(l,b)
# main()

def greatest(a,b,c)->int:
    if(a>b and a>c):
        print("a is greatest")
    elif(b>a and b>c):
        print("b is greatest")
    else:
        print("c is greatest")
def main():
    a=int(input("enter a"))
    b=int(input("enter b"))
    c=int(input("enter c"))
    greatest(9,b,c)
main()