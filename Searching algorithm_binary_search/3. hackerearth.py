# Problem Description
# Its been a few days since Charsi is acting weird. And finally you(his best friend) came to know that its because his proposal has been rejected.
# He is trying hard to solve this problem but because of the rejection thing he can’t really focus. Can you help him? The question is: Given a number n , find if n can be represented as the sum of 2 desperate numbers (not necessarily different) , where desperate numbers are those which can be written in the form of (a*(a+1))/2 where a > 0 .
# Input :
# The first input line contains an integer n (1<=n<=10^9).
# Output :
# Print “YES” (without the quotes), if n can be represented as a sum of two desperate numbers, otherwise print “NO” (without the quotes).


# solution describption and how to solve  in binary search :
# https://chatgpt.com/c/2190e5b0-3b7c-4089-b3c7-b05258e67282 from chatgpt link

import math

def binary_search(low, high, key):
    while low <= high:
        mid = (low + high) // 2
        x = mid * (mid + 1)
        if x < key:
            low = mid + 1
        elif x > key:
            high = mid - 1
        else:
            return mid
    return -1

def main():
    n = int(input())
    flag = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        b = n - (i * (i + 1)) // 2
        y = binary_search(1, int(math.sqrt(2 * b)), 2 * b)
        if y > 0:
            flag = 1
            break
    if flag == 1:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
