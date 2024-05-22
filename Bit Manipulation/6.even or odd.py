def print_binary(num):
    for i in range(7, -1, -1):
        print((num >> i) & 1, end='')      
    print()
    
if __name__ == "__main__":
    n = int(input("Enter the number for finding the equivalent binary nubmer  : "))
    print_binary(n)
    
    if n&1:
        print(f"{n} is odd number  ")
    else:
        print(f"{n} is even number")
        
        
    print(n<<1)     #n*2 . shortly to find multiplication  by 2
    print(n>>1)     #n/2 . shortly to find the divide by 2
    
    
    