# ∑i=1 to n( i*(n-i+1)) = 1*n + 2*(n-1) +....n*1
n = int(input("Take the integer input: "))
t_sum = 0
for i in range(1, n + 1):
    t_sum += i * (n - i + 1)
print(f"The total sum of the series: {t_sum}")

# using formula
total = n * (n + 1) * (n + 2) / 6  # Corrected the formula
print(f"The total sum using formula: {total}")

# using list comprehension
total_sum = sum([i * (n - i + 1) for i in range(1, n + 1)])
print(f"The total sum using list comprehension: {total_sum}")
