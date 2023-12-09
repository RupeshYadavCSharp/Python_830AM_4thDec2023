#program to add frst and last digit

num = int(input("Enter any 4 digit number "))  #num = 1234
a = num % 10          #1234 % 10 = 4
b = num // 1000       #1234 // 1000 = 1

sum = a + b
print("sum is ",sum)



