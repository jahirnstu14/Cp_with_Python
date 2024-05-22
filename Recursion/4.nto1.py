def nto1(n):
    if n==0:
        return
    print(n) # return karar projonto ai area cholbe  cholbe be .
    nto1(n-1)

n = int(input())
nto1(n)