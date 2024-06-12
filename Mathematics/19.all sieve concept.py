# Constants
N = int(2e6 + 10)

# Arrays
a = [0] * N
hp = [0] * N
canRemove = [0] * N

# Function to find distinct prime factors of x using the hp array
def distinctPf(x):
    ans = []
    while x > 1:
        pf = hp[x]
        if not ans or ans[-1] != pf:  # only add if it's a new prime factor
            ans.append(pf)
        while x % pf == 0:
            x //= pf
    return ans

# Sieve of Eratosthenes to find smallest prime factor for each number
for i in range(2, N):
    if hp[i] == 0:
        for j in range(i, N, i):
            if hp[j] == 0:
                hp[j] = i

# Reading the input for n and q
n, q = map(int, input().split())

# Reading the array a
for _ in range(n):
    a_i = int(input())
    a[a_i] += 1  # Increment the count for this number in a

# Marking the numbers which can be removed
for i in range(1, N):
    if a[i] > 0:
        canRemove[i] = 1

# Processing the queries
for _ in range(q):
    x = int(input())
    pf = distinctPf(x)

    isPossible = False
    for i in range(len(pf)):
        for j in range(i, len(pf)):
            product = pf[i] * pf[j]
            if i == j and x % product != 0:
                continue
            toRemove = x // product
            if toRemove < N and canRemove[toRemove] == 1:
                isPossible = True
                break
        if isPossible:
            break
    
    if isPossible:
        print("Yes")
    else:
        print("No")
