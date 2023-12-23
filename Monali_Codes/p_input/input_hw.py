l=int(input("enter lenght:"))
b=int(input("enter breath:"))
area=l*b
print("Area of rectangle is",area)


cel=int(input("enter temperature"))
f=(cel*9/5)+32
print("fahrenheit is",f)

math=float(input("enter marks in maths:"))
chem=float(input("enter marks in chem:"))
phy=float(int(input("enter marks in phy:")))

total=math+chem+phy

percent=(total/300)*100
print("total marks is",total)
print("Percent got is",percent)

piz=100
puffs=20
coldd=10

a=int(input("enter the no. of pizza bought:"))
b=int(input("enter the no. of puffs bought:"))
c=int(input("enter the no. of cold drinl bought:"))

print("Bill Details")
print("No of pizzas:",a)
print("No of puffs", b)
print("No of cold drink bought",c)

print("Total price=",a*piz+b*puffs+c*coldd)
print("ENJOY THE SHOW!!!")


total_population=80000
total_men=52/100*80000
total_lit=48/100*80000
total_lit_men=35/100*80000
total_lit_women=(48-35)/100*80000
print("Total no. of literate women are",total_lit_women)
print("Total no. of literate mens are",total_lit_men)