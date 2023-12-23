#code for reversing 4 digit no
num=int(input("enter 4 digit number :"))         #4927
fd=num//1000                                   #fd=4927//1000=4
sd=(num//100)%10                               #sd=(4927//100)%10=9
td=(num%100)//10                               #td=(4927%100)//10=2
ld=num%10                                      #ld=4927%10=7
nnum=ld*1000+td*100+sd*10+fd*1                 #nnum=7*1000+td*100+sd*10+fd*1=7294
print("reverse no is",nnum)