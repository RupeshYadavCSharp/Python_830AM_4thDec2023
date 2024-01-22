matchstick=21
while(True):
    user=int(input("user pick"))
    matchstick=matchstick-user
    print("remaining matchstick",matchstick)
    computer=5-user
    print("computer pick", computer)
    matchstick=matchstick-computer
    print("remaing is",matchstick)
    if(matchstick==1):
        print("computer win")


