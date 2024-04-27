a = int(input("the first number is :"))
b = int(input("the second  number is :"))
c = int(input("the third   number is :"))

if a<=b and a<c:
    smallest = a
    if b<c :
        middle = b
        largest =c
        
elif b<=a and b<=c:
    smallest = b
    if a<c:
        middle=a
        largest=b
else:
    smallest = c
    if a<b:
        middle=a
        largest=b

print(f"the ascending order will be for {a},{b},{c} are {smallest},{middle},{largest}")

# using sorted function 

# ascending_order = sorted([a,b,c])

# smallest = ascending_order[0]
# middle = ascending_order[1]
# largest = ascending_order[2]

# 35print(f"the ascending order will be for {a},{b},{c} are {smallest},{middle},{largest}")
    
    
