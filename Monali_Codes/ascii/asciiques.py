# ch=input("enter any character")
# ch = ord(ch)
#
# if(ch>=65 and ch<=90):
#     print("Capital letter")
# elif(ch>=97 and ch<=122):
#     print("Small letter")
# elif(ch>=48 and ch<=57):
#     print("its a digit")
# else:
#     print("its a special symbol")


ch=input("enter any character:")
ch=ord(ch)

if(ch>=65 and ch<=90):
    print("its capital letter")
elif(ch>=97 and ch<=122):
    print("its small letter")
elif(ch>=48 and ch<=57):
    print("its a digit")
else:
    print("its a special character")
