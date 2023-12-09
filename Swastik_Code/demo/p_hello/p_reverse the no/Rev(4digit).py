# code for reversing 4 digit number
num = int(input("enter 4 digit no\n",))                      #1234
a = num % 10                                                 #a=4
b = (num % 100) // 10                                        #b=3
c = (num // 100) % 10                                        #c=2
d = num // 1000                                              #d=1
e = 1000*a + 100*b + 10*c + 1*d                              #e=1000*4+100*3+10*2=10*1
print ("reverse of 4 digit no is",e)                         #reverse of 4 digit no is 4321
