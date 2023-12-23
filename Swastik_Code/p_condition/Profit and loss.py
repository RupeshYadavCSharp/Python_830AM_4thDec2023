#code for finding profit and loss after selling product
costp=float(input("enter cost price :"))                  #enter cost price: 1000
sellp=float(input("enter selling price :"))               #enter selling price: 2000
if(costp<sellp):                                          #profit after selling is (2000-1000)=1000
    print("profit after selling is",sellp-costp)
else:
    print("loss after selling is",costp-sellp)