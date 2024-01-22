def greatest(a,b,c)->int:
    numbers = [a, b, c]
    greatestno = max(numbers)
def main():
    a=int(input("enter first digit"))
    b=int(input("enter second digit"))
    c=int(input("enter third digit"))
    numbers=greatest(a,b,c)
    print("greatest no is",numbers)
main()