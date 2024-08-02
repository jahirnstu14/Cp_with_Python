# nice solution : https://takeuforward.org/data-structure/shortest-common-supersequence-dp-31/
    
def shortestSupersequence(s1, s2):
    n = len(s1)
    m = len(s2)

    dp = [[0 for i in range(m + 1)] for j in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = 0
    for i in range(m + 1):
        dp[0][i] = 0

    for ind1 in range(1, n + 1):
        for ind2 in range(1, m + 1):
            if s1[ind1 - 1] == s2[ind2 - 1]:
                dp[ind1][ind2] = 1 + dp[ind1 - 1][ind2 - 1]
            else:
                dp[ind1][ind2] = 0+ max(dp[ind1 - 1][ind2], dp[ind1][ind2 - 1])

    len_ = dp[n][m]
    i = n
    j = m

    index = len_ - 1
    ans = ""

    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            ans += s1[i - 1]
            index -= 1
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            ans += s1[i - 1]
            i -= 1
        else:
            ans += s2[j - 1]
            j -= 1
    #Adding Remaing Characters - Only one of the below two while loops will run 
    while i > 0:
        ans += s1[i - 1]
        i -= 1
    while j > 0:
        ans += s2[j - 1]
        j -= 1

    ans=ans[::-1]
    return ans

def main():
    s1 = "brute"
    s2 = "groot"
    print("The Longest Common Supersequence is " + shortestSupersequence(s1, s2))

if __name__ == "__main__":
    main()