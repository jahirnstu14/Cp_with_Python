def nto1(n):
    if n==0:
        return
    # return karar projonto ai area cholbe  cholbe be 
    nto1(n-1)
    # return karar por ei area cholbe 
    print(n)

n = int(input())
nto1(n)


# for recursion time complexity we can find 
# number of functions calls ---> n
# each function complexity ---->1
# total complexity will be = n * 1
