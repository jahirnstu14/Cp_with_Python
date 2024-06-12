a,b = map(int,input().split())

print(f"{a} is used as dividen and {b } is used as divisor : ")
gcd = a

while b!=0:
    gcd = b
    b = a%b
    a = gcd
print(gcd)




# using recursion 

def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)


a,b = map(int,input().split())
print(gcd(a,b))