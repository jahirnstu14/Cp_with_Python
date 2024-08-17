def phi(n):
    result = n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            while n % i == 0:
                n //= i
            result -= result // i
    if n > 1:
        result -= result // n
    return result

# User-defined input

t = int(input())
while t: 
    n = int(input("Enter a number: "))
    print("The value of phi(", n, ") is:", phi(n))
    t-=1