import math
import sys

# Constants
MOD = 1000000007
EPS = 1e-9
M_PI = 3.14159265358979323846
MAXN = 1000000 + 5

# Initialize arrays
isPrime = [0] * MAXN
cnt = [0] * MAXN

def gcd(a, b):
    """Compute the greatest common divisor of a and b."""
    return a if b == 0 else gcd(b, a % b)

def lcm(a, b):
    """Compute the least common multiple of a and b."""
    return a * (b // gcd(a, b))

def mod_exp(b, p, m):
    """Compute (b^p) % m efficiently."""
    x = 1
    while p:
        if p & 1:
            x = (x * b) % m
        b = (b * b) % m
        p >>= 1
    return x

def exp(b, p):
    """Compute b^p efficiently."""
    x = 1
    while p:
        if p & 1:
            x *= b
        b *= b
        p >>= 1
    return x

def sieve():
    """Perform the sieve of Eratosthenes to mark non-prime numbers."""
    isPrime[0] = isPrime[1] = 1
    for i in range(2, int(math.sqrt(1000000)) + 1):
        if isPrime[i] == 0:
            if i * i <= 1000000: # it is optional. if i don't use it , there is no problem in solutio . it will give same output 
                for j in range(i * i, 1000001, i):
                    isPrime[j] = 1

def to_be_afraid(num):
    """Check if a number is 'afraid'."""
    tmp_num = num
    dig = 0
    while num > 0:
        if num % 10 == 0:
            return False
        dig += 1
        num //= 10

    div = exp(10, dig - 1)
    num = tmp_num
    while num > 0:
        num %= div
        div //= 10
        if num != 0 and isPrime[num] == 1:
            return False
    return True

def precal():
    """Precompute the counts of 'afraid' primes."""
    for i in range(2, 1000001):
        cnt[i] = cnt[i - 1]
        if isPrime[i] == 0:
            if to_be_afraid(i):
                cnt[i] += 1

def main():
    """Main function to read input and output the results."""
    sieve()
    precal()
    
    t = int(input().strip())
    results = []
    for _ in range(t):
        n = int(input().strip())
        results.append(str(cnt[n]))
    
    print("\n".join(results))

if __name__ == "__main__":
    main()
