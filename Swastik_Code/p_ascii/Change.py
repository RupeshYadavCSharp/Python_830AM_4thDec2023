ch=input("enter character")
ch=ord(ch)
if(ch>=65 and ch<=90):
    ch=ch+32
    print(chr(ch))
elif(ch>=97 and ch<=122):
    ch=ch-32
    print(chr(ch))