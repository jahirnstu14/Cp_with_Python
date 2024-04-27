def factorialn(n):
    factorial = 1

    if n <= 1:
        return factorial
    else:
        for i in range(1, n+ 1):
            factorial *= i  # Multiply factorial by each integer from 1 to num
        return factorial


n = int(input("Enter the n value : "))
r = int(input("Enter the c value : "))

if r>n or r<0:
    print("The value of binomial coeficient is {0}")
    
else:
    numerator = factorialn(n)
    denominator = factorialn(r)*factorialn(n-r)
    binomial_coe = numerator // denominator
    print(f"The binomial coeficint of the number is {binomial_coe}")