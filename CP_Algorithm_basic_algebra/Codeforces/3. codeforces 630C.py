# problem link :https://codeforces.com/problemset/problem/630/C
# logic : https://codeforces.com/problemset/problem/630/C

def max_lucky_numbers(n):
    # Calculate the maximum number of unique lucky numbers up to n digits
    return 2 * (2 ** n - 1)

# Read input
n = int(input().strip())

# Output the result
print(max_lucky_numbers(n))


# using left shift 

def max_lucky_numbers(n):
    # Calculate the maximum number of unique lucky numbers up to n digits
    power_of_two = 1 << n  # This is 2^n
    return 2 * (power_of_two - 1)

# Read input
n = int(input().strip())

# Output the result
print(max_lucky_numbers(n))