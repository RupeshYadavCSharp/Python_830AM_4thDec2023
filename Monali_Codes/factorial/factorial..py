num=int(input("enter any number="))
if(num<0):
    print("Factorials are not defined for negative number")

else:
    result=1
    for i in range(1,num+1):
        result=result*i
        print("Factorial of",num,"is",result)

import math

number = int(input("Enter a number to check if it's a pronic number: "))

sqrt_num = int(math.sqrt(number))
if sqrt_num * (sqrt_num + 1) == number:
    print(f"{number} is a pronic number.")
else:
    print(f"{number} is not a pronic number.")
