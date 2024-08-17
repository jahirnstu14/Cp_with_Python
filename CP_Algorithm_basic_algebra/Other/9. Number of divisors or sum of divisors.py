# If a prime factor p appears e times in the prime factorization of n , then we can use the factor p upt to e times in the subset. Which means we have e + 1 choices. therefore if the prime factoriazation of n is p1^e1 . p2^e2 . p2^e2 .... pk^ek, where pi are distainct prime number , then the number of divisors is : d(n) = (e1+1) . (e2+1) .(e3+1) ... (ek+1) . if there is only one distinct prime divisor n = p1^e1, then there are oviously e1+1 divisors(1,p1,p1^2,p^3 ... p^3)

# number of divisor 

def number_of_divisors(num):
    total = 1
    i = 2
    while i * i <= num:
        if num % i == 0:
            e = 0
            while num % i == 0:
                e += 1
                num //= i
            total *= (e + 1)
        i += 1
    if num > 1:
        total *= 2
    return total

def main():
    # Reading the number of test cases
    t = int(input("Enter the number of test cases: ").strip())
    
    results = []
    
    # Processing each test case
    for _ in range(t):
        num = int(input("Enter the number: ").strip())
        result = number_of_divisors(num)
        results.append(result)
    
    # Printing results
    for res in results:
        print(res)

if __name__ == "__main__":
    main()

# find the divisor 

def find_divisors(n):
    # Initialize a list of empty lists for storing divisors
    div = [[] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(i, n + 1, i):
            div[j].append(i)
    
    return div

def main():
    # Define the maximum value N
    N = 100010
    
    # Find divisors for all numbers up to N
    divisors = find_divisors(N)
    
    # Reading the number of test cases
    t = int(input("Enter the number of test cases: ").strip())
    
    # Processing each test case
    for _ in range(t):
        num = int(input("Enter the number: ").strip())
        # Print the divisors of the number
        if num <= N:
            print(f"Divisors of {num}: {' '.join(map(str, divisors[num]))}")
        else:
            print("Number out of range")

if __name__ == "__main__":
    main()


# Sum of divisors

# In general , for n is p1^e1 . p2^e2 . p2^e2 .... pk^ek, we receive formula for sum of divisor :
#     sigma(n) = ((p1^e1+1 - 1)//(p1 - 1)) . ((p2^e2+1 - 1)//(p2 - 1)) .... ((pk^ek+1 - 1)//(pk - 1))

def sum_of_divisors(num):
    total = 1
    i = 2
    while i * i <= num:
        if num % i == 0:
            e = 0
            while num % i == 0:
                e += 1
                num //= i

            sum_divisors = 0
            pow_i = 1
            while e > 0:
                sum_divisors += pow_i
                pow_i *= i
                e -= 1
            total *= sum_divisors
        i += 1

    if num > 1:
        total *= (1 + num)
    
    return total

# User-defined input
try:
    num = int(input("Enter a number: "))
    result = sum_of_divisors(num)
    print("Sum of divisors:", result)
except ValueError:
    print("Please enter a valid integer.")



