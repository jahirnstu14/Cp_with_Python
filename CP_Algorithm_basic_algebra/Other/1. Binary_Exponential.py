# this is used to find the x is raised to power n  =>  x^n

# nice number theory basic in one blog : https://progkriya.org/gyan/basic-number-theory

# using most efficient way

def binpow(a, b):
    res = 1
    while b > 0:
        if b & 1:
            res = res * a
        a = a * a
        b >>= 1
    return res

# Example usage
a = int(input("Enter the base (a): "))
b = int(input("Enter the exponent (b): "))
print(f"{a} raised to the power of {b} is {binpow(a, b)}")


# same thing can be done by using recursion 

def binpow(a, b):
    if b == 0:
        return 1
    res = binpow(a, b // 2)
    if b % 2:
        return res * res * a
    else:
        return res * res

# Example usage
a = int(input("Enter the base (a): "))
b = int(input("Enter the exponent (b): "))
print(f"{a} raised to the power of {b} is {binpow(a, b)}")

# for for big integer a or b 

def binpow(a, b, m):
    a %= m
    res = 1
    while b > 0:
        if b & 1:
            res = res * a % m
        a = a * a % m
        b >>= 1
    return res

# Example usage
a = int(input("Enter the base (a): "))
b = int(input("Enter the exponent (b): "))
m = int(input("Enter the modulus (m): "))
print(f"{a} raised to the power of {b} modulo {m} is {binpow(a, b, m)}")

# note : it's possible to speed this algorithm for large b>>m. if m is a prime number x^n = x^n mod (m-1) for prime m , and x^n = x^n mod 0(m) (mod m ) for composite number . first is fermat's little therorem and second is the Eulur's theorem .'