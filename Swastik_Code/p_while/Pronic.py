#pronic number code

import  math

num = int(input("Enter any number "))
n = int(math.sqrt(num))

if( (n * (n + 1))== num ):
    print("pronic ")
else:
    print("not pronic ")


