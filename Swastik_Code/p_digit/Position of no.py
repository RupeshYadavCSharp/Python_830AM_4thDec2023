#code for interchanging position of digits on tens place with digit on 100 place
num=int(input("enter any four digit no\n"))         #4927
fd=num//1000                                        #fd=4927//1000=4
sd=(num//100)%10                                    #sd=(4927//100)%10=9
td=(num%100)//10                                    #td=(4927%100)//10=2
ld=num%10                                           #ld=4927%10=7
nnum=fd*1000+td*100+sd*10+ld*1                      #nnum=4000+200+90+7=4297
print("new no after interchanging digits is",nnum)  #new no after interchanging digits is 4297