def powerofn(x,n):
    pow=1
    
    while n>0:
        if n&1:
            pow*=x
        
        x*=x
        n>>1
    return pow

n = int(input())
x = int(input())

print(powerofn(x,n))



# for 2 to power n is using bit 

# 1<<0 = 1 =1
# 1<<1 = 2 =10
# 1<<3 = 4 =100
# 1<<4 = 8 =1000

# so,1<<n = 2^n