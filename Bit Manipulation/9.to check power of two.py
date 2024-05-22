
n = int(input("Enter the number to check power of 2 or not : "))
if(n&n-1):
    print("the number is not power of two ")
else:
    print("The number is  power of two ")
    
    
    
# it is the simple logice we know that if n is 2 to the power = 00010000000 and n-1 = 00001111111 . if we do AND operation it will give the 0. then we can call n is power of 2. or not zero n is not power of 2.



