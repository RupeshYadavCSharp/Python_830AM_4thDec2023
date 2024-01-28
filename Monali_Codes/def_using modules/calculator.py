def rectangle(l,b)->tuple:
    area=l*b
    perimeter=2*(l+b)
    return area,perimeter

def main():
    l=int(input("enter l"))
    b=int(input("enter b"))
    area,perimeter=rectangle(l,b)
    print("area is",area,"perimeter is",perimeter)
main()