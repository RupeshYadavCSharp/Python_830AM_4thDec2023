#code for calculating marks
maths=float(input("enter marks obtained in maths:"))                    #enter marks obtained in maths=80
chem=float(input("enter marks obtained in chem:"))                      #enter marks obtained in chem:=80
phy=float(input("enter marks obtained in phy:"))                        #enter marks obtained in phy:=80
print("each paper consist of 100")
print("total marks consist is",100*3)                                   #total marks consist is 300
total=maths+chem+phy                                                    #total marks obtained is=80+80+80=240
print("total marks obtained is",total)
print("total percentage is",((total/300)*100))                          #total percentage is 240/300*100=80
