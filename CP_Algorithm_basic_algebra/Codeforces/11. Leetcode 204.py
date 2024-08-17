def count_primes(n):
    if n <= 2:
        return 0

    not_prime = [False] * n
    count = 0
    
    for i in range(2, n):
        if not not_prime[i]:
            count += 1
            for j in range(i * 2, n, i):
                not_prime[j] = True
    
    return count


def main():
    # User input for the number n
    n = int(input("Enter a number: "))

    # Calling the count_primes function and printing the result
    result = count_primes(n)
    print(f"The number of prime numbers less than {n} is: {result}")

if __name__ == "__main__":
    main()


# Another solution 
class Solution:
    def countPrimes(self, n: int) -> int:
        # Handle edge cases where n is less than or equal to 2
        if n <= 2:
            return 0
        
        # Prime number generation using the Sieve of Eratosthenes
        prime = [True] * n
        prime[0] = prime[1] = False
        
        for i in range(2, int(n ** 0.5) + 1):
            if prime[i]:
                for j in range(i * i, n, i):
                    prime[j] = False
        
        # Counting prime numbers
        prime_count = sum(prime)
        
        return prime_count
