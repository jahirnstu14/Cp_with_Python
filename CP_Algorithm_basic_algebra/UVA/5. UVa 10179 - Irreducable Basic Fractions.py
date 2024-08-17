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
    
# problem logic : https://gocodergo.wordpress.com/2017/07/05/uva-10179-irreducable-basic-fractions/

# same problem : 
# 1. uva 10299 - Relatives