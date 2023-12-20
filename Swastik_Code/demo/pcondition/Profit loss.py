#code for profit and loss statement
cp=int(input("enter cost price\n"))                   #1000
sp=int(input("enter selling price\n"))                #2000
if(cp<sp):                                            #2000>1000
    print("profit after selling is Rs",sp-cp)         #profit after selling is Rs 2000-1000=1000
else:
    print("loss after selling is Rs",cp-sp)

