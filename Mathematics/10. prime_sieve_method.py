# if q<=10^7 , N = 10^7 previous method will not work 

n = int(input())

prime_number = [1] * n

prime_number[0]=prime_number[1]=0

for i in range(2,n):
    if prime_number[i]==1:  # if this condition is existed time complexity will be : n/2+n/3+n/5+n/7+n/11 = n(1/2+1/3+1/5...) = n * log(log(n))
        for j in range(2*i,n,i):
            prime_number[j] = 0
            
# otherwise we donot consider if condition , then the complexity will be 0(n) = n/2 + n/3 + n/4 + n/5....+n/n = n(1/2+1/3+1/4+1/5...) = n * log(n) 
            

query = int(input())
while query:
    query-=1
    num =int(input())
    if prime_number[num]:
        print(f"{num} is prime number ")
    else:
        print(f"{num} is not prime number ")
        
             
            