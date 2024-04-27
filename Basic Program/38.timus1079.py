
dp=[0]*10010
dp[0]= 0
dp[1]=1

for i in range(1,10000//2):
    dp[2*i]=dp[i]
    dp[2*i+1]=dp[i]+dp[i+1]
    

while True:
    n = int(input(""))
    if n==0:
        break
    
    mx = max(dp[:n+1])
    print(f"The maximu number upto {n} is {mx}")
    
    
