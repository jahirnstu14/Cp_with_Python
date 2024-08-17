# logic discussion link : https://www.tushers.com/uva-11327-enumerating-rational-numbers/


import math
from bisect import bisect_left

N = 200000 + 5
phi = [0] * N

def ETFPre():
    global phi
    phi[0] = 0
    phi[1] = 2
    for i in range(2, N):
        phi[i] = i

    for i in range(2, N):
        if phi[i] == i:
            for j in range(i, N, i):
                phi[j] -= phi[j] // i

    for i in range(2, N):
        phi[i] += phi[i - 1]

def main():
    ETFPre()
    
    while True:
        k = int(input())
        if k == 0:
            break
        
        if k == 1:
            print("0/1")
            continue
        
        if k == 2:
            print("1/1")
            continue

        LB = bisect_left(phi, k)  # to find denominator
        sub = k - phi[LB - 1]  # position of numerator
        
        cnt = 0
        for i in range(1, LB + 1):
            if math.gcd(i, LB) == 1:
                cnt += 1
                if cnt == sub:
                    print(f"{i}/{LB}")
                    break

if __name__ == "__main__":
    main()
