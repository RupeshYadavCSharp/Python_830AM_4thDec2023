num = int(input("Enter any number "))

flag = True

for i in range(2,num):     #2 to 6
    if(num % i == 0):
        flag = False
        break

if(flag == True):
    print("Prime number ")
else:
    print("Not prime number")