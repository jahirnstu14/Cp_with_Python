# problem link : https://codeforces.com/contest/1916/problem/B
# problem solution and logic : https://codeforces.com/blog/entry/124138

import math

def solve():
    t = int(input().strip())
    results = []
    
    for _ in range(t):
        a, b = map(int, input().strip().split())
        
        if b % a == 0:
            # Case 1: b is a multiple of a
            k = b // a
            x = b * k
        else:
            # Case 2: General case
            g = math.gcd(a, b)
            x = a * b // g
        
        results.append(x)
    
    for result in results:
        print(result)
solve()


