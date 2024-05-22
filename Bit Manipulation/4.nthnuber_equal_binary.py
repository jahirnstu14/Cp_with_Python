def print_binary(num):
    for i in range(8, -1, -1):
        print((num >> i) & 1, end='')      
    print()
    
# The bitwise AND operation with 1 is used to extract the least significant bit (LSB) of the number after it has been right-shifted.

# Here's a detailed explanation:
# Right Shift Operation (>>): When you right-shift a number by i positions, you are effectively dividing the number by 
# 2^i  
# and discarding the remainder. For instance, if the number is 9 (which is 1001 in binary) and you right-shift it by 2 positions, you get 10 in binary (which is 2 in decimal).

if __name__ == "__main__":
    n = int(input("Enter the number for finding the equivalent binary nubmer  : "))

    print_binary(n)
    
    
    
    