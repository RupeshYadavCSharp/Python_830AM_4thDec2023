ch=input("enter character")
ch=ord(ch)
if(ch>=65 and ch<=90):
    print("capital letter")
elif(ch>=97 and ch<=122):
    print("small letter")
elif(ch>=48 and ch<=57):
    print("digit")
else:
    print("special character")