# integer factorization using trivial 

def trial_division(n):
    factorization = []
    for d in range(2, int(n**0.5) + 1):
        while n % d == 0:
            factorization.append(d)
            n //= d
    if n > 1:
        factorization.append(n)
    return factorization

# User-defined input
n = int(input("Enter the number to factorize: "))

# Get prime factorization
factors = trial_division(n)

# Print the factors
print(f"The prime factors of {n} are: {factors}")


# Wheel factorization:
    
# This is an optimization of the trial division. Once we know that the number is not divisible by 2, we don't need to check other even numbers. This leaves us with only 50% of the numbers to check. After factoring out 2, and getting an odd number, we can simply start with 3 and only count other odd numbers.

def trial_division2(n):
    factorization = []
    # Handle the factor of 2 separately
    while n % 2 == 0:
        factorization.append(2)
        n //= 2
    # Check odd factors from 3 onwards
    for d in range(3, int(n**0.5) + 1, 2):
        while n % d == 0:
            factorization.append(d)
            n //= d
    # If n is still greater than 1, it must be a prime factor
    if n > 1:
        factorization.append(n)
    return factorization

# User-defined input
n = int(input("Enter the number to factorize: "))

# Get prime factorization
factors = trial_division2(n)

# Print the factors
print(f"The prime factors of {n} are: {factors}")

# Precomputed primes

# Extending the wheel factorization method indefinitely, we will only be left with prime numbers to check. A good way of checking this is to precompute all prime numbers with the Sieve of Eratosthenes until sqrt(n) ,and test them individually.

# this sieve can be used most of the time 

def sieve(limit):
    is_prime = [True] * (limit + 1)
    for p in range(2, int(limit**0.5) + 1):
        if is_prime[p]:
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
    prime_numbers = []
    for p in range(2, limit + 1):
        if is_prime[p]:
            prime_numbers.append(p)
    return prime_numbers

# Define the list of primes
primes = []

def trial_division4(n):
    factorization = []
    for d in primes:
        if d * d > n:
            break
        while n % d == 0:
            factorization.append(d)
            n //= d
    if n > 1:
        factorization.append(n)
    return factorization

# User-defined input for the number to factorize
n = int(input("Enter the number to factorize: "))

# User-defined input for the upper limit to generate prime numbers
limit = int(input("Enter the upper limit for generating prime numbers: "))

# Generate the list of prime numbers up to the given limit
primes = sieve(limit)

# Get prime factorization
factors = trial_division4(n)

# Print the factors
print(f"The prime factors of {n} are: {factors}")

# Fermat's factorization method

# mathematical proof : https://mathworld.wolfram.com/FermatsFactorizationMethod.html

# Fermat's factorization method tries to exploit this fact by guessing the first square a^2 , and checking if the remaining part, b^2 = a^2 - n . is also a square number. If it is, then we have found the factors . 

import math

def fermat(n):
    a = math.ceil(math.sqrt(n))
    b2 = a * a - n
    b = round(math.sqrt(b2))
    while b * b != b2:
        a += 1
        b2 = a * a - n
        b = round(math.sqrt(b2))
    factor1 = a - b
    factor2 = a + b  # The other factor
    return factor1, factor2

def main():
    n = int(input("Enter an integer n: "))
    factor1, factor2 = fermat(n)
    print(f"The factors of {n} are: {factor1} and {factor2}")

if __name__ == "__main__":
    main()

    
# This factorization method can be very fast if the difference between the two factors p and q is small. The algorithm runs in 0(|p-q|) . 


# it is the basic of prime factorization . i always use it . 

def factorization(n):
    count = 0
    while n % 2 == 0:
        count += 1
        n //= 2
    if count > 0:
        print(f"2^{count}", end=" ")
    
    for i in range(3, int(n**0.5) + 1, 2):
        count = 0
        while n % i == 0:
            count += 1
            n //= i
        if count > 0:
            print(f"{i}^{count}", end=" ")
    
    # this condition only for prime number 
    
    if n > 2:
        print(f"{n}^1", end="")

def main():
    while True:
        n = int(input())
        if n == 0:
            break
        factorization(n)
        print()

if __name__ == "__main__":
    main()
