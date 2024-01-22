balance=0
def readbalance():
    global balance
    balance=int(input("enter your balance"))

def withdrawmoney():
    global balance
    withdraw=int(input("enter amount to withdraw"))
    balance=balance-withdraw
def depositmoney():
    global balance
    deposit=int(input("enter amount to deposit"))
    balance=balance+deposit


def main():
    print(int(input("enter balance")))
    print(withdrawmoney())
    print(depositmoney())

main()

