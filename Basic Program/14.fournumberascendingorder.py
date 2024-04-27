a = int(input("the first number is :"))
b = int(input("the second  number is :"))
c = int(input("the third   number is :"))
d = int(input("the fourth   number is :"))

if a>b:
    a,b = b,a
if a>c:
    a,c=c,a
if a>d:
    a,d =d,a
if b>c:
    b,c=c,b
if b>d:
    b,d =d,b
if c>d:
    c,d =c,d
print(f"the ascending value are :{a},{b},{c},{d}")







    