def is_prime(n):
    if n==1:
        return False
    if n==2:
        return True
    limit = int(n**0.5)
    for i in range(2,limit+1):
        if(n%i==0):
            return False
            break
    return True
           
        

num = int(input("Enter the number of interger : "))
if is_prime(num):
    print(f"{num} is prime number ");
else:
    print(f"{num} is not prime number ");
    
    