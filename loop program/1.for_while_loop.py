n = int(input("take the input the last number :"))
# 1to n print using loop
print("The List of Natural Numbers from 1", "to", n) 
 
for i in range(1,n+1,1):
    print(i,end=" ")
print()
print(f"The List of Natural Numbers {n} to 1")   
for i in range(n,0,-1):
    print(i,end=" ")

print()

print("odd number between 1 to n")
for i in range(1,n,2):
    print(i,end=" ")
    
print()
print("use the while loop :")
i=5
while(i<=7):
    num=i*2
    i=i+1
    print(num,end=" ")