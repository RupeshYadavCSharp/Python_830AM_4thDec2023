#code for reversing four digit number
num=int(input("enter 3 digit no :"))          #num=543
fd=num//100                                   #fd=543//100=5
sd=(num%100)//10                              #sd=(543%100)//10=4
ld=num%10                                     #ld=543%10=3
nnum=ld*100+sd*10+fd*1                        #nnum=3*100+4*10+5*1=543
print("reverse num is",nnum)