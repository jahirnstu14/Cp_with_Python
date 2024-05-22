def print_binary(num):
    for i in range(7, -1, -1):
        print((num >> i) & 1, end='')      
    print()
    
if __name__ == "__main__":
    # A=ord('A')
    # E = ord('E')
    
    # for i in range(A,E+1):
    #     print(chr(i))
    #     print_binary(i)
        
    # a=ord('a')
    # z = ord('e')
    
    # for i in range(a,z+1):
    #     print(chr(i))
    #     print_binary(i)
    
    convert_to_smaller = ord('A')
    after_convert = convert_to_smaller|(1<<5)
   
    print(chr(after_convert))
    
     # we know that A is equal to binary number : 01000001 and a binary number is a=1100001 so, the difference is that for A is convert to a we need it transfer into 5th bit into set . for that we do OR operation . between 10000001 = "A" and 00100000=1<<5 
     
    convert_to_smaller = ord('a')
    after_convert = convert_to_smaller& (~(1<<5))
    print(chr(after_convert))
    
    # we know that a binary number is a=11000001 and  A is equal to binary number : 01100001. so, the difference is that for a is convert to a we need it transfer into 5th bit into unset . for that we do invert and then AND operation . between 10000001 = "A" and 00100000=1<<5 