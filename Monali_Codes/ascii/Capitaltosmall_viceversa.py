# ch=input("enter any character")
# ch=ord(ch)
#
# if(ch>=65 and ch<=90):
#     ch=ch+32
#     print(chr(ch))
# else:
#     ch=ch-32
#     print(chr(ch))


# ch=input("enter any character")
# ch=ord(ch)
#
# if(ch>=65 and ch<=90):
#     print("its a capital no.")
# elif(ch>=97 and ch<=122):
#     print("its a small no.")
# elif(ch>=48 and ch<=57):
#     print("its a digit")
# else:
#     print("its a special symbol")

# ch=input("enter any character")
# ch=ord(ch)
#
# if(ch>=65 and ch<=90):
#     ch=ch+32
#     print(chr(ch))
#
# else:
#     ch=ch-32
#     print(chr(ch))
#
# code to convert capital letter to small and vice versa:-

ch=input("enter any character:")
ch=ord(ch)

if(ch>=65 and ch<=90):
    ch=ch+32
    print(chr(ch))
else:
    ch=ch-32
    print(chr(ch))