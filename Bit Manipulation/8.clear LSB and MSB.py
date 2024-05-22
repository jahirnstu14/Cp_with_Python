def print_binary(num):
    for i in range(8, -1, -1):
        print((num >> i) & 1, end='')      
    print()
    
if __name__ == "__main__":
    n = int(input("Enter the number for finding the equivalent binary nubmer  : "))

    print_binary(n)
    i=4
    
    clear_lsb = (n& (~((1<<(i+1))-1)))
    print_binary(clear_lsb)
    
    
    
    # for clear lsb upto 4th bit position 
    
    # we know that 59 = 000111011. for making it 000100000 ,
    # first 111100000 AND operation with 000111011 . but to represent 111100000 is difficult . for this it convert into 000011111 and it can be find from 100000(1<<i+1)-1 = 000011111
    # so, after making it inverse we find 111100000 which is the first number we do AND operation with 000111011
    
    # for 3 msb clear_lsb
    
    i=3
    clear_msb = (n& ((1<<(i+1))-1))
    print_binary(clear_msb)
    
    # we know that 59 = 000111011. for making it 000001011 ,
    # first 000001111 AND operation with 000111011 . but to represent 000001111 is difficult . for this find from 10000(1<<i+1)-1 = 00001111
    
    
    
    