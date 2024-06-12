
# https://www.spoj.com/problems/ZSUM/

# equation : 2(n-1)^k + 2(n-1)^n-1 + n^k + n^n =  2((n-1)^k + (n-1)^n-1) + n^k + n^n 



M = int(1e9 + 7)
mode = int (1e7+7)
def binary_exponenet(base,power):
    ans = 1
    while power>0:
        if power&1:
            ans = (ans * base) % M
        base = (base * base)% M
        power>>=1
    return ans  

if __name__ == "__main__":
    
    n,k = map(int,input().split())
    if n==0 or k==0:
        print(0)
        
    else:
        ans1 = (2*(binary_exponenet(n-1,k) % mode + binary_exponenet(n-1,n-1)%mode)%mode)%mode
        ans2 = (binary_exponenet(n,k)%mode + binary_exponenet(n,n)%mode)%mode
        final_answer = ans1 + ans2
        print(final_answer)
    