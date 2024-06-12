
#  using recursion 

# M = int(1e9 + 7)

# def binary_exponenet(base,power):
#     if power==0:
#         return 1
#     res = binary_exponenet(base,power//2)
#     if power&1:
#         return (base * ((res * res)%M ))%M
#     else:
#         return (res * res) % M
        

# base,power = map(int,input().split())
# print(binary_exponenet(base,power));


# using iterative method 

M = int(1e9 + 7)
def binary_exponenet(base,power):
    ans = 1
    while power>0:
        if power&1:
            ans = (ans * base) % M      # the complexity of this function is logb(b number of bits in binary of power )
        base = (base * base)% M
        power>>=1
    return ans       


base,power = map(int,input().split())
print(binary_exponenet(base,power));




# for a >10^18 and b is 2^1024 . it is going to out of range for this we do multiplication function  . it is important 
# M = int(1e9 + 7)
# def binary_exponenet(base,power):
#     ans = 1
#     while power>0:
#         if power&1:
#             ans = multiply_bigmod(ans,base) % M      
#         base = multiply_bigmod(base,base)% M
#         power>>=1
#     return ans  



# def multiply_bigmod(base, power):
#     ans = 0
#     while power>0:
#         if power&1:
#             ans = (ans + base) % M     # this is used when base of number is greater than 10^18 because, base*base = 10^18 * 10^18 is not possible.  
#         base = (base + base)% M
#         power>>=1
#     return ans  
         


# base,power = map(int,input().split())
# print(binary_exponenet(base,power));