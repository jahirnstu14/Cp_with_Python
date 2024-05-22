def print_binary(num):
    for i in range(7, -1, -1):
        print((num >> i) & 1, end='')      
    print()
    
if __name__ == "__main__":
    n = int(input("Enter the number for finding the equivalent binary nubmer  : "))

    print_binary(n)
    a=n
    i=1 # represent ith bit position
    
    if(a&(1<<i))!=0:
        print(f"{i}th bit set")
    else:
        print(f" {i}th bit is not set ")
    
    # for set bit ith position  
    print_binary(a |1<<i )
    
    print("inverse the binary number : ")
    print_binary(~n)
    
    # unset the ith bit position
    print_binary(a&(~(1<<i)))
    
    # for exor operation for doing toogle any ith position it can be 1 position or 2 or so on.
    # toogle 
    # The XOR operation toggles the bit at position i:
    # If the bit is 0, it becomes 1.
    # If the bit is 1, it becomes 0.
    print_binary(a^(1<<i))
    
    
#    Combining a | 1 << i:

# The expression a | 1 << i sets the i-th bit of the variable a to 1.
# Suppose a is 5 (binary 0101) and i is 1:
# 1 << 1 results in 10 (binary for 2).
# a | 10 results in 0101 | 0010, which is 0111 (binary for 7).
# Essentially, this operation ensures that the bit at position i in a is set to 1, regardless of its previous value.

# for a&(~(1<<i))
# if 5=101, for doing inverse 010 we use ~5. it is use for convert 0 to 1 and 1 to 0 . example : 10001000 if i want to make 01110111 then we use ~.

# if we want to unset the ith value of number. then we do AND operation of number and ith bit 1 toggle usinng ~. 
# example:the number is 10001. and we want to unset 4th bit then , we can write 10000 then we convert it into 01111 . and do and operation 
# 10001
# 01111 AND operation 
# 00001 (so 4th bit now unset)