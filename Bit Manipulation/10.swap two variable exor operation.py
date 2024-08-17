# two swap two number using exor

a=6
b=10
# we also know formula a^0=a and a^a=a
a = a^b
b=b^a
# b = b^(a^b)=>b^a^b = b^b^a=0^a=a so,b=a
a = a^b 
# a = a^(b^a)=>a^b^a=>a^a^b=>0^b=b,so,a=b

print(f"the value of a is  {a}  and b is  {b} are swapping each other ")

