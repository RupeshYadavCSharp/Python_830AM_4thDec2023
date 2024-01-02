ch=input("enter any character")
ch=ord(ch)
if(ch>=65 and ch<=90):
    ch=ch+32
    print(chr(ch))
else:
    ch=ch-32
    print(chr(ch))