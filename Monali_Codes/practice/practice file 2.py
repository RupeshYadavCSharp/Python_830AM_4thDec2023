import time
matchstick=21
while(True):
    user=int(input("user pick"))
    matchstick=matchstick-user
    print("remaining matchstick is", matchstick)

    computer=5-user
    print("computer pick",computer)
    matchstick=matchstick-computer
    print("remaining matchstick is",matchstick)
    if(matchstick==1):
        print("user loose")
        break