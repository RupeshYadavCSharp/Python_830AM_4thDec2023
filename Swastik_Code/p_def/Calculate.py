def calc(n1,n2):
    a = n1 + n2
    s = n1 - n2
    m = n1 * n2
    d = n1 // n2

    return a,s,m,d

def main():
    a,s,m,d = calc(12, 2)
    print("add is ",a )
    print("sub is ",s )
    print("mul is ",m )
    print("div is ",d )
main()
