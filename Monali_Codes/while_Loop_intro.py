# i=1
# while(i<11):
#     print(i,end=" ")
#     i+=1


# num=int(input("enter any number;-"))
# count=0
# while(num!=0):
#     num=num//10
#     count+=1
# print("its a ",count,"digit number")


# num=int(input("enter any number:-"))
# count=0
# while(num!=0):
#     num=num//10
#     count+=1
# print("its a ",count,"digit number")


#
# i=1
# while(i<11):
#     print(i,end=" ")
#     i+=1

#
# i=2
# while(i<10):
#     print(i,end=" ")
#     i+=1

# i=5
# # while(i<50):
# #     print(i,end=" ")
# #     i+=1
# num=int(input("enter any number:-"))
# count=0
# while(num!=0):
#     num=num//10
#     count+=1
# print("you have entered",count,"digit number")



# num=int(input("enter any number:-"))
#
# count=0
# while(num!=0):
#     num=num//10
#     count+=1
# print("you have entered a",count,"digit number")

#
# for i in range(1,6):
#     for j in range(i):
#         print("*",end=" ")
#     print()

# for i in range(1,6):
#     for j in range(i):
#         print("*",end=" ")
#     print()
#
# for i in range(1,6):
#     for j in range(6-i):
#         print("*", end=" ")
#     print()


# num=int(input("enter any number:-"))
# large=0
# while(num!=0):
#     rem=num%10
#     if(rem>large):
#         large=rem
#     large=large-rem
# print(large)

num=int(input("enter any number:-"))
small=9


while(num!=0):
    rem=num%10
    if(rem<small):
        small=rem
    num=num//10
print(small)

