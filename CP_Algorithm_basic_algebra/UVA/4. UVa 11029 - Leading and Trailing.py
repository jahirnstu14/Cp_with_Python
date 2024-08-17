# logic behind the problem : https://st3inum.github.io/posts/uva-11029/

# Logarithmic Properties
# Logarithms and Exponents:

# The logarithm of a number 
# 𝑥 (base 10) can be expressed as:log10(𝑥)=integer part+fractional part log 10
# For a number x, the integer part of 
# log10(𝑥)  gives the order of magnitude, and the fractional part gives the leading digits.

# Why This Works

# Logarithms and Powers:
# When you take the logarithm of a number, you break it down into its magnitude and its significant digits. The fractional part of the logarithm tells you the leading digits when the number is expressed in scientific notation.
# For example, if log10(1234)≈3.091, the integer part (3) tells you the number is in the thousands, and the fractional part (0.091) tells you that 
# 1234= 10^0.091 * 1000


import math

def bigmod(b, p, m):
    if p == 0:
        return 1
    xx = bigmod(b, p // 2, 1000)
    xx = (xx * xx) % 1000
    if p % 2 == 1:
        xx = (xx * b) % 1000
    return xx

def main():
    t_case = int(input().strip())
    
    while t_case:
        n, k = map(int, input().strip().split())

        # Executing first 3 digits
        
        x = k * math.log10(n)
        x = x - int(x)  # Taking fractional value only
        ans = math.pow(10, x)
        ans = ans * 100 # for taking threee leading digit 

        print(f"{int(ans)}...", end="")

        # Executing last 3 digits
        print(f"{bigmod(n, k, 1000):03d}")

        t_case -= 1

if __name__ == "__main__":
    main()
