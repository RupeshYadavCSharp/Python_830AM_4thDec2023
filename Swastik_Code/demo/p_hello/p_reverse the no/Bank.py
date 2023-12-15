#code for withdrawal money
num=int(input("enter amount\n"))             #1360
fh=num//500                                #fh=1360//500=2
fh1=num%500                                #fh1=1360%500=360
print("500 *",fh)                          #500 * 2
th=fh1//200                                #th=360//200=1
th2=fh1%200                                #th2=360%200=160
print("200 *",th)                          #200 * 1
hd=th2//100                                #hd=160//100=1
hd1=th2%100                                #hd1=160%100=60
print("100 *",hd)                          #100 * 1
ft=hd1//50                                 #ft=60//50=1
ft1=hd1%50                                 #ft1=60%50=10
print("50 *",ft)                           #50 * 1
tr=ft1//10                                 #tr=10//10
tr1=ft1%10                                 #tr1=10%10
print("10 *",tr)                           #10 * 1