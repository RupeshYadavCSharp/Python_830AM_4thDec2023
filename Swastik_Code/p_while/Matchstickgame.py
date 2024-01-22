#Match Stick GAME
import  time

matchstick = 21

while(True):
    user = int(input("User Pick "))
    matchstick = matchstick - user

    print("remaining match stick ",matchstick)

    comp = 5 - user
    time.sleep(5)

    print("Computer picked ",comp)

    matchstick = matchstick - comp
    print("remaining match stick ", matchstick)

    if(matchstick == 1):
        print("USer Loose ")
        break
