# We try to find a non-trivial divisor, by checking if any of the numbers between 2 and sqrt(n) is a divisor of n . If it is a divisor, then n
# is definitely not prime, otherwise it is. 

def is_prime(x):
    if x < 2:
        return False
    for d in range(2, int(x**0.5) + 1):
        if x % d == 0:
            return False
    return True

# Get user input
x = int(input("Enter a number to check if it is prime: "))
if is_prime(x):
    print(f"{x} is a prime number.")
else:
    print(f"{x} is not a prime number.")


# Fermat primality test to determine a number is prime or not 

# Fermat's little theorem (see also Euler's totient function) states, that for a prime number p and a coprime integer p the following equation holds:
# a^p-1 = 1 mod p . In general this theorem doesn't hold for composite numbers.This can be used to create a primality test. We pick an integer 2<=a<=p-2 and check if the equation holds or not. If it doesn't hold, means a^p-1 is not equal to 1 mod p . so, p cannot be a prime number. p and a are coprime . 

import random

def binpower(a, b, m):
    result = 1
    base = a % m
    while b > 0:
        if b % 2 == 1:
            result = (result * base) % m
        base = (base * base) % m
        b //= 2
    return result

def probably_prime_fermat(n, iter=5):
    if n < 4:
        return n == 2 or n == 3

    for _ in range(iter):
        a = random.randint(2, n - 2)
        if binpower(a, n - 1, n) != 1:
            return False
    return True

# Get user input
n = int(input("Enter a number to check if it is probably prime: "))
if probably_prime_fermat(n):
    print(f"{n} is probably a prime number.")
else:
    print(f"{n} is not a prime number.")
    
# for becoming coprime a,n each other , it must be hold condition :  gcd(a, n) = 1
# The Fermat test is still being used in practice, as it is very fast and Carmichael numbers are very rare. E.g. there only exist 646 such numbers below 10^9 .
















