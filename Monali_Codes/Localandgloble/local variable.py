def show():
    x=10
    print("is show x=",x)
def main():
    show()
    print("main =",x)
main()

# it will show error because local variable constrain to only that fuction and cannot be seen by other fuction.
# 1. made inside the fuction
# 2.local scope----means only seen by the fuction in which the variable is made
# 3.local life-----life of variable ends as the fuction terminates
