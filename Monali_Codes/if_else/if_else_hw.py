num=int(input("enter any num:-"))
if(num%2==0):
    print("its an even number")
else:
    print("its an odd number")



cost_p=int(input("enter cost price:"))
sell_p=int(input("enter selling price:"))
if(sell_p>cost_p):
    print("you are in profit of",sell_p-cost_p)
else:
    print("you are in loss of",cost_p-sell_p)