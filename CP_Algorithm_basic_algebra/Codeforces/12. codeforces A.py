# problem link : https://codeforces.com/contest/26/problem/A

def count_two_prime_factors(n):
    count = 0

    for i in range(2, n + 1):
        temp = i  # Use a temporary variable to avoid modifying `i`
        facto = []

        # Find prime factors of `temp`
        for j in range(2, temp + 1):
            if temp % j == 0:
                if j not in facto:
                    facto.append(j)
                while temp % j == 0:
                    temp //= j

        # Check if there are exactly two distinct prime factors
        if len(facto) == 2:
            count += 1

    return count

def main():
    n = int(input("Enter a number: ").strip())
    result = count_two_prime_factors(n)
    print(result)

if __name__ == "__main__":
    main()
