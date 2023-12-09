num = int(input("Enter any 3 digit number "))   #num = 123

a = num % 10              #123 % 10 = 3

b = (num // 10) % 10      #123 // 10 = 12 % 10 = 2

c = num // 100            #123 // 100 = 1

rev = a * 100 + b * 10 + c*1
print("rev is ",rev)

