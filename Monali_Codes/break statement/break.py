# for i in range(1,11):
#     if(i==5):
#         break
#     print(i,end=" ")
#
# print("out of loop")

# for i in range(1,6):
#     if(i==4):
#         break
#     print(i,end=" ")
# print("out of loop")

for i in range(1,8):
    if(i==7):
        break
    print(i,end=" ")
print("out of loop")

num=int(input("enter any number:-"))
flag=True

for i in range(2,num):
    if(num%i==0):
        flag=False


if(flag==True):
    print("its a prime number")
else:
    print("its not a prime number")
