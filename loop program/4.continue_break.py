# print the odd number upto n using continue

n = int(input("Enter the integer number :"))
for i in range(1,n):
    if(i%2==0):
        continue
    else:
        print(i,end=" ")
        
# print 1,2,3
for i in  range(1,n):
    if(i>3):
        break
    else:
        print(i,end=" ")
        
        

    