# code for reversing the number
num = int(input("enter 3 digit number\n",))           # 213
a = num % 10                                          # a=3
b = (num // 10) % 10                                  # b=21=21//10=1
c = num // 100                                        # c=2
d = a*100 + b*10 + c*1                                # d=300+20+1=321
print ("reverse number is",d)                         # reverse no is 312