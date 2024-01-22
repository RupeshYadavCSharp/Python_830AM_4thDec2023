count = int(input("Enter count "))  #10

f = 0
s = 1

print(f , " ", s, end = " " )

for i in range(1,count - 1):    #same as for i in range(1,11):
    t = f + s
    print(t,end = " ")
    f = s
    s = t
