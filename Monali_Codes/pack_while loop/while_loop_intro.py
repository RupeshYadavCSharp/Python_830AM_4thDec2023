# i=1
# while(i<11):
#     print(i)
#     i+=1
#
# i=2
# while(i<16):
#     print(i)
#     i+=1


# num=int(input('enter any number='))
# count=0
# while(num!=0):
#     num=num//10
#     count+=1
# print("you have entered",count,"digit  number")

# num=int(input("enter any number="))
# count=0
# while(num!=0):
#     num=num//10
#     count+=1
# print("You have entered",count,"digit number")

# num=int(input("enter any number:-"))
# sum=0
# while(num!=0):
#     rem=num%10
#     sum=sum+rem
#     num=num//10
# print("sum is",sum)

# num=int(input("enter any number:="))
# sum=0
# while(num!=0):
#     rem=num%10
#     sum=sum+rem
#     num=num//10
# print("sum is",sum)
#
#
#
# num=int(input("enter any number:="))
# sum=0
# while(num!=0):
#     rem=num%10
#     sum=sum+rem
#     num=num//10
# print("sum is",sum)

# num=int(input("enter any number="))
# large=0
# while(num!=0):
#     rem=num%10
#     if(rem>large):
#         large=rem
#     num=num//10
# print("largest number is",large)

#
# num=int(input("enter any number:="))
# small=9
# while(num!=0):
#     rem=num%10
#     if(rem<small):
#         small=rem
#     num=num//10
# print("Smallest number is",small)

#
# num=int(input("enter any number:-"))
# large=0
# while(num!=0):
#     rem=num%10
#     if(rem>large):
#        large=rem
#     num=num//10
# print("The largest number is",large)
#
# num=int(input("enter any number"))
# small=9
# while(num!=0):
#     rem=num%10
#     if(rem<small):
#         small=rem
#     num=num//10
# print(small)


import time
matchstick=21

while(matchstick!=1):
    user=int(input("user pick"))
    matchstick=matchstick-user

    print("remaining match stick", matchstick)


    computer=5-user
    print("computer pick is",computer)
    matchstick=matchstick-computer
    print("The remainig match stick is", matchstick)


















# num=int(input("enter any number="))
# flag=True
# for i in range(2,num):
#     if(num%i==0):
#         flag=False
#
# if(flag==True):
#     print("its a prime number")
# else:
#     print("its not a prime number")




