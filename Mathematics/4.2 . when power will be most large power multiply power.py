
# for most large power 

M = int(1e9 + 7)
def binary_exponenet(base,power,m):
    ans = 1
    while power>0:
        if power&1:
            ans = (ans * base) % m      # the complexity of this function is logb(b number of bits in binary of power )
        base = (base * base)% m
        power>>=1
    return ans       


# for 50^64^32 % M  .

# first we find binary exponent for (64^32 % M), SECODND FIND 5O^SOMETING RETURN % M 

# A^b mod M  = a^(b mod 0(M) 0 is phi function ) % M

print(binary_exponenet(50,binary_exponenet(64,32,M-1),M));

# M-1 for NUMBER OF coprime of prime number M is M-1