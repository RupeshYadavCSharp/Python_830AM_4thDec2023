#code for withdrawing money from bank
num=int(input("enter amount\n"))                   #num=1360
print("500 * ",num//500)                           #500 * 2
af=num%500                                         #af=1360%500=360
print("200 * ",af//200)                            #200 * 1
at=af%200                                          #at=360%200=160
print("100 * ",at//100)                            #100 * 1
ah=at%100                                          #ah=160%100=60
print("50 * ",ah//50)                              #50 * 1
afy=ah%50                                          #afy=60%50=10
print("10 * ",afy//10)                             #10 * 1