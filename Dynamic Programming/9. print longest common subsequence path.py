

# nicely describe solution : https://takeuforward.org/data-structure/print-longest-common-subsequence-dp-26/



def lcs(s1, s2):
    n = len(s1)
    m = len(s2)
    
    dp = [[0 for j in range(m + 1)] for i in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = 0
    for i in range(m + 1):
        dp[0][i] = 0

    for ind1 in range(1, n + 1):
        for ind2 in range(1, m + 1):
            if s1[ind1 - 1] == s2[ind2 - 1]:
                dp[ind1][ind2] = 1 + dp[ind1 - 1][ind2 - 1]
            else:
                dp[ind1][ind2] = 0+max(dp[ind1 - 1][ind2], dp[ind1][ind2 - 1])

    len_ = dp[n][m]
    i = n
    j = m
    
    index = len_ - 1
    str_ = ""
    for k in range(1,1+len_):
      str_+="$" #dummy string
    
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            str_ = s1[i - 1] + str_[:-1]
            index -= 1
            i -= 1
            j -= 1
        elif s1[i - 1] > s2[j - 1]:
            i -= 1
        else:
            j -= 1
    
    print("The Longest Common Subsequence is", str_)

def main():
    s1 = "abcde"
    s2 = "bdgek"
    
    lcs(s1, s2)

if __name__ == "__main__":
    main()
    
    
# Output: The Longest Common Subsequence is bde

# Time Complexity: O(N*M)

# Reason: There are two nested loops

# Space Complexity: O(N*M)