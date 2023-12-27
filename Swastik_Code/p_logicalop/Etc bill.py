#code for finding electricity bill by using units
unit=float(input("enter unit consumes\n"))            #enter unit consumes 670
if(unit>=1 and unit<=100):
    unit1=unit*3
    print("bill is",unit1,"Rs")
elif(unit>=101 and unit<=300):
    a=unit%100
    b=unit-a
    print("bill is",b*3+a*5,"Rs")
elif(unit>300):                                       #670>300(True)
    a=100                                             #a=100
    b=200                                             #b=200
    c=unit-(a+b)                                      #c=670-(100+200)=370
    print("bill is",a*3+b*5+c*7,"Rs")                 #bill is 100*3+200*5+370*7=3890.0 Rs
