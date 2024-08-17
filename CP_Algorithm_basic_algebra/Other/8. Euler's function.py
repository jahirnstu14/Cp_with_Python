# Euler's totient function, also known as phi-function O(n), counts the number of integers between 1 and n inclusive, which are coprime to n. Two numbers are coprime if their greatest common divisor equals 1.

# Here is an implementation using factorization in 0(sqrt(n))

def phi(n):
    result = n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            while n % i == 0:
                n //= i
            result -= result // i
    if n > 1:
        result -= result // n
    return result

# User-defined input
n = int(input("Enter a number: "))
print("The value of phi(", n, ") is:", phi(n))



# Euler totient function from 1 to n in 0(n loglogn )

def phi_1_to_n(n):
    phi = list(range(n + 1))  # Initialize phi with values 0 to n
    
    for i in range(2, n + 1):
        if phi[i] == i:  # i is a prime number
            for j in range(i, n + 1, i):
                phi[j] -= phi[j] // i

    return phi

# User-defined input
n = int(input("Enter a number: "))
phi_values = phi_1_to_n(n)

# Display the results
for i in range(1, n + 1):
    print(f"phi({i}) = {phi_values[i]}")
    


# divisor sum property 

# ∑0(d) = n , Here the sum is over all positive divisors d of n . For instance the divisors of 10 are 1, 2, 5 and 10. Hence  0(1) + 0(2) + 0(5) + 0(10) = 10

# Finding the totient from 1 to n  using the divisor sum property
# more worse complexity : 0(n logn )

def phi_1_to_n(n):
    phi = list(range(n + 1))  # Create a list with values from 0 to n
    phi[0] = 0
    phi[1] = 1
    
    for i in range(2, n + 1):
        phi[i] = i - 1

    for i in range(2, n + 1):
        for j in range(2 * i, n + 1, i):
            phi[j] -= phi[i]

    return phi

# Input handling
n = int(input("Enter the value of n: "))
result = phi_1_to_n(n)
print("Euler's Totient function values from 1 to", n)
for i in range(1, n + 1):
    print(f"phi({i}) = {result[i]}")

# Application in Euler's theorem
# The most famous and important property of Euler's totient function is expressed in Euler's theorem:
# a^0(m) = 1 mod m , where a and m are relatively prime 

# In the particular case when m is prime, Euler's theorem turns into Fermat's little theorem:
# a^(m-1 ) = 1 mod m 

# Euler's theorem and Euler's totient function occur quite often in practical applications, for example both are used to compute the modular multiplicative inverse.
# As immediate consequence we also get the equivalence:
    
# a^n = a^(n mod 0(m)) mod m , This allows computing  x^n mod m for very big n .
    
    


 

































