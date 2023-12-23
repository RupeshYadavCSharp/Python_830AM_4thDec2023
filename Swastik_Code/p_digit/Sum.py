#code for sum of first and last digit num
num=int(input("enter any 4 digit no\n"))              #num=1234
firstd=num//1000                                      #firstd=1234//1000=1
lastd=num%10                                          #lastd=1234%10=4
sum=firstd+lastd                                      #sum=1+4=5
print("sum of first and last digit is",sum)           #sum of first and last digit is 5