a = [0]*10
print(a)

for i in range(1,5+1):
    id=int(input("Enter the id number is : "))
    a[id-1]+=1
    
max = 0
for i in range(10):
    if a[i]>max:
        max=a[i]
        
        
print(max)
    