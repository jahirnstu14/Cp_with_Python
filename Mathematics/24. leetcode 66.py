digit  = list(map(int,input().split()))
n = len(digit)
fact = 1
for  i in range(n-1,-1,-1):
    if digit[i] < 9:
        digit[i]+=1
        print(digit)
        fact=0
        break
    digit[i] = 0
if fact:  
    newnumber = [0] * (n+1)
    newnumber[0]=1
    print(newnumber)
