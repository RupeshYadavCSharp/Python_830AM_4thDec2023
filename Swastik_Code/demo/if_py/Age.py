age = int(input("enter age:"))
if(age>18):
    print("can vote")
else:
    print("cannot vote")
    a = 18-age
    print ("you can vote after",a,"years")