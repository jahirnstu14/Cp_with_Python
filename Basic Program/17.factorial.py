num = int(input("Enter the integer number to compute its factorial: "))

factorial = 1

if num <= 1:
    print(f"The factorial of number {num}! is {factorial}")
else:
    for i in range(1, num + 1):
        factorial *= i  # Multiply factorial by each integer from 1 to num
    print(f"The factorial of number {num}! is {factorial}")
