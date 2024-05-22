
# for 1<<0 = 1 (binary)=>1(decimal)=2^0
#     1<<1 =10         =>2         =2^1
#     1<<2 =100        =>4         =2^2
#     1<<3 =1000       =>8         =2^3
    
#     so for finding 2 to power n . we can write 1<<n. it will calculate 2^n .
    
    
n = int(input())
print(1<<n) 
# without using any power calculate only bit manipulaation

# for c++ 
print(1<<32-1) 

# for c++ we know that the interger number can be store upto 32 bit . so, the maximum number can be store which value will be 2^32-1. but to represent 2^32 we need 33 bit for this resason it donot calculate anything beacuse , overflow . if the value is unsigned it maximum number can be store 2^31 - 1 because , 1 most significant bit is used to represent the sign negative or positive. for negative bit is 1 and positive bit is 0.
# if declear unsigned then it calulate 2^32-1 . because , it only store positive number  and no sign bit is used . 