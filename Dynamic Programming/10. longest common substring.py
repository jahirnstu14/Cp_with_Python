# nice discussion of the code is : https://takeuforward.org/data-structure/longest-common-substring-dp-27/

# 1. usisng tabulation method

def lcs(s1, s2):
    n = len(s1)
    m = len(s2)
    
    # Create a DP table with dimensions (n+1) x (m+1) initialized to zeros
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Initialize a variable 'ans' to keep track of the maximum LCS length
    ans = 0
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                # If the characters match, increment LCS length by 1
                val = 1 + dp[i - 1][j - 1]
                dp[i][j] = val
                ans = max(ans, val)
            else:
                # If the characters do not match, reset LCS length to zero
                dp[i][j] = 0
    
    # 'ans' contains the length of the Longest Common Substring
    return ans

def main():
    s1 = "abcjklp"
    s2 = "acjkp"

    print("The Length of Longest Common Substring is", lcs(s1, s2))

if __name__ == '__main__':
    main()


# 2. using reducing space complexity:


def lcs(s1, s2):
    n = len(s1)
    m = len(s2)
    
    # Initialize two arrays 'prev' and 'cur' to store the LCS lengths
    prev = [0 for i in range(m + 1)]
    cur = [0 for i in range(m + 1)]

    # Initialize a variable 'ans' to keep track of the maximum LCS length
    ans = 0
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i-1] == s2[j-1]:
                # If the characters match, increment LCS length by 1
                val = 1 + prev[j-1]
                cur[j] = val
                ans = max(ans, val)
            else:
                # If the characters do not match, reset LCS length to zero
                cur[j] = 0
        prev = cur[:]  # Update 'prev' with the values of 'cur'
    
    # 'ans' contains the length of the Longest Common Substring
    return ans

def main():
    s1 = "abcjklp"
    s2 = "acjkp"

    print("The Length of Longest Common Substring is", lcs(s1, s2))

if __name__ == '__main__':
    main()



