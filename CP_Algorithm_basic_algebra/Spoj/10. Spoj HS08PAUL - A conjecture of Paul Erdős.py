import math

N = 10000007
mark = [True] * N  # Array to mark primes, initialized to True
ans = [0] * N  # Array to store results

def seive(n):
    """Performs the sieve of Eratosthenes to mark non-prime numbers."""
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if mark[i]:
            for p in range(i * i, n, i * 2):
                mark[p] = False

def main():
    seive(N)  # Perform sieve to mark primes
    for x in range(1, 5001):
        for y in range(1, 91):
            res = x * x + y * y * y * y  # Calculate the expression
            if res >= N:
                break
            if mark[res] and (res % 2 == 1 or res == 2):  # Check if result is prime and odd or 2
                ans[res] = 1
    
    # Prefix sum to accumulate results
    for i in range(1, N):
        ans[i] = ans[i] + ans[i - 1]
    
    T = int(input("Enter number of test cases: ").strip())  # Read number of test cases
    results = []
    for _ in range(T):
        n = int(input().strip())  # Read each test case
        results.append(str(ans[n]))  # Collect results
    
    print("\n".join(results))  # Print all results at once

if __name__ == "__main__":
    main()
