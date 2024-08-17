
# time complexity : 0(log(log(n)))
# def sieve_of_eratosthenes(n):
#     is_prime = [True] * (n + 1)
#     is_prime[0] = is_prime[1] = False
    
#     for i in range(2, int(n**0.5) + 1):
#         if is_prime[i]:
#             for j in range(i * i, n + 1, i):
#                 is_prime[j] = False
                
#     return is_prime

# n = 100  # Example value for n
# primes = sieve_of_eratosthenes(n)
# print(primes)
# Sieving by the odd numbers only¶
# Since all even numbers (except  
# $2$ ) are composite, we can stop checking even numbers at all. Instead, we need to operate with odd numbers only.


import math
#  an implementation that counts the number of primes smaller than or equal to  
# $n$  using block sieving.
def count_primes(n):
    S = 10000

    primes = []
    nsqrt = int(math.sqrt(n))
    is_prime = [True] * (nsqrt + 2)
    for i in range(2, nsqrt + 1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i * i, nsqrt + 1, i):
                is_prime[j] = False

    result = 0
    block = [True] * S
    for k in range((n // S) + 1):
        block = [True] * S
        start = k * S
        for p in primes:
            start_idx = (start + p - 1) // p
            j = max(start_idx, p) * p - start
            while j < S:
                block[j] = False
                j += p
        if k == 0:
            block[0] = block[1] = False
        for i in range(min(S, n - start + 1)):
            if block[i]:
                result += 1

    return result

n = 100  # Example value for n
print(count_primes(n))


# need to find all prime numbers in a range  
# $[L,R]$  of small size (e.g.  
# $R - L + 1 \approx 1e7$ )

import math

def segmented_sieve(L, R):
    # Generate all primes up to sqrt(R)
    lim = int(math.sqrt(R))
    mark = [False] * (lim + 1)
    primes = []
    for i in range(2, lim + 1):
        if not mark[i]:
            primes.append(i)
            for j in range(i * i, lim + 1, i):
                mark[j] = True

    is_prime = [True] * (R - L + 1)
    for i in primes:
        start = max(i * i, (L + i - 1) // i * i)
        for j in range(start, R + 1, i):
            is_prime[j - L] = False
    if L == 1:
        is_prime[0] = False
    return is_prime

L, R = 10, 30  # Example values for L and R
primes = segmented_sieve(L, R)
print(primes)
