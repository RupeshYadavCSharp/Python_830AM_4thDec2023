# code for withdrawal of money from bank
num = int(input("enter amount\n",))
print ("500 *",num//500)
a = num - (num//500*500)
print ("200 *",(a//200))
b = ((num - ((num//500)*500))//200*200)
print ("100 *",(b//100))
