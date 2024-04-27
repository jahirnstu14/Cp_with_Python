# n = int(input("take the one integer :"))

# if n>=0:
#     summation = (n*(n+1))/2
#     print(f"the sum for 1 to n for interger number is {summation}");
# else:
#     n=-n
#     summation =1-(n*(n+1))/2
#     print(f"the sum for 1 to negative number {n} is {summation}");

n = int(input())

if n>=0:
    print(int((n*(n+1))/2))
else:
    k=-n
    print(int(1-(k*(k+1))/2))
    
# a=int(input())
# if a>0:
#     print(int(a*(a+1)/2))
# else:
#     c=-a
#     print(int(1-c*(c+1)/2))