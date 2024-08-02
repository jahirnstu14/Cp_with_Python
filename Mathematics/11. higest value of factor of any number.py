# to find highest primefactor and lowest prime factor of number

n = int(input())  

prime_number = [1] * n

primefactor_highest = [0] * n
primefactor_lowest = [0] * n

primefactor_highest[1] = primefactor_lowest[1] = 1

prime_number[0]=prime_number[1]=0

for i in range(2,n):
    if prime_number[i]==1: 
        for j in range(2*i,n,i):
            primefactor_highest[i] = primefactor_lowest[i] = i 
            prime_number[j] = 0
            primefactor_highest[j]=i        #in this statement is written for find highest prime factor . beacuse , j is multiple of i. and take the higest multiple of i . it can be more than one time this way it will be replace again and again same value.
            if primefactor_lowest[j]==0:  # in this statement is written for find fighest prime factor . default is 0. after execute 1 times the value will be replaced by i . second time will not execute for this same value . example : 10 = 2 * 5 . has higest value 5, lowest 2
                primefactor_lowest[j]=i
                               
for i in range(1,100):
    print(f"the highest and lowest primefactor of {i} : {primefactor_highest[i]} and {primefactor_lowest[i]}")
                