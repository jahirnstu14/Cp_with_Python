# problem link : https://premsvmm.blogspot.com/2015/06/project-euler-2-even-fibonacci-numbers.html

import sys

def main():
    t = int(input().strip())  # Read the number of test cases

    for _ in range(t):
        n = int(input().strip())  # Read each value of n
        
        a, b, s = 1, 2, 0  # Initialize the first two Fibonacci numbers and the sum
        
        while b <= n:
            if b % 2 == 0:
                s += b  # Add to sum if the Fibonacci number is even
                
            a, b = b, a + b  # Generate the next Fibonacci number
            
        print(s)  # Print the sum of even Fibonacci numbers up to n

if __name__ == "__main__":
    main()
