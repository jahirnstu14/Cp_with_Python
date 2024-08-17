# problme link : https://codeforces.com/problemset/problem/630/B
# logic : https://codeforces.com/blog/entry/24160

import math

# Input: initial number of transistors and time in seconds
n, t = map(int, input().split())

# Growth rate per second
growth_rate = 1.000000011

# Calculate the number of transistors after t seconds
result = n * (growth_rate ** t)

# Output the result with high precision
print(f"{result:.12f}")

# it can also be done by implementing binary exponentiation 
