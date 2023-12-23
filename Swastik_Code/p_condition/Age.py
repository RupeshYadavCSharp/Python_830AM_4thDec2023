#code to check you can vote or not
age=int(input("enter age\n"))                        #age=19                     #age=14
if(age>18):                                          #if(19>18):(true)           #if(14>18):(false)
    print("you can vote")                            #you can vote               #you can vote after 18-14= 4 years
else:
    print("you can vote after",18-age,"years")