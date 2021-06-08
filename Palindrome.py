"""I used the code from Module 3: Exploration: Dynamic Programming - Longest Common Subsequence Problem
to help solve this problem. I took the provided code and altered it to fit this problem"""


def lcs_BF_helper(s1, s2, m,n):
    if m < 0 or n < 0:
        return 0;
    elif s1[m] == s2[n]:
        return 1 + lcs_BF_helper(s1, s2 , m-1, n-1)
    else:
        return max(lcs_BF_helper(s1, s2, m-1 , n), lcs_BF_helper(s1, s2, m, n-1))

def checkPalindrome_1(string, k):
    length = len(string)
    str2 = string[::-1]
    x =  lcs_BF_helper(string,str2, len(string)-1, len(str2)-1)
    return True if x >= k else False



def lcs_topdown_helper(s1, s2, m, n, dp):

    # base case
    if (m == 0 or n == 0):
        return 0

    # If the subproblem already computed return it
    if (dp[m - 1][n - 1] != -1): return dp[m - 1][n - 1]

    # if the chars match, store result
    if (s1[m - 1] == s2[n - 1]):
        dp[m - 1][n - 1] = 1 + lcs_topdown_helper(s1, s2, m - 1, n - 1, dp)
        return dp[m - 1][n - 1]

    else:
        dp[m - 1][n - 1] = max(lcs_topdown_helper(s1, s2, m - 1, n, dp), lcs_topdown_helper(s1, s2, m, n - 1, dp))
        return dp[m - 1][n - 1]

def checkPalindrome_2(string, k):
    m = n = len(string)
    str2 = string[::-1]
    dp = [[-1 for x in range(n + 1)] for x in range(m + 1)]
    x =  lcs_topdown_helper(string, str2, m, n, dp)
    return True if x >= k else False
