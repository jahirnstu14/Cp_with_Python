
a= int(input())
b=int(input())
mask = 0xffffffff

while b:
    sum = (a^b)& mask # without carry using exor and mask is used the limmit the exor value upto mask value . its limit the value
    carry =((a&b)<<1) & mask
    a = sum
    b = carry
    
if a>>31 & 1:
    print(~(a^mask))
print(a)

# without bit operation 

# list1 = [a,b]
# print(sum(list1))
    