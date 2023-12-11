# code for withdrawal of money from bank
num = int(input("enter amount\n",))
print ("500 *",num//500)
a = num - (num//500*500)
print ("200 *",(a//200))
b = a // 200
print ("100 *",(num - ((500*(num//500))+(200*(b))))//100)
c = (a - b) // 100
print ("50 *", a - (c // 100)