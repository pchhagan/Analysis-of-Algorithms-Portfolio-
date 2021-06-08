def patternmatch(string, p):
    string_len = len(string)
    pattern_len = len(p)

    dp = [[0 for x in range(pattern_len + 1)] for x in range(string_len + 1)]
    dp[0][0] = 1

    for i in range(1, pattern_len+1):
        if p[i-1] == "*":
            dp[0][i] = dp[0][i-1]

    for i in range(1, string_len + 1):
        for j in range(1, pattern_len+1):
            if string[i-1] == p[j-1] or p[j-1] == "?":
                dp[i][j] = dp[i-1][j-1]
            elif p[j-1] == "*":
                dp[i][j] = dp[i-1][j-1] or dp[i][j-1] or dp[i-1][j]

    return True if dp[-1][-1] == 1 else False





print(patternmatch("abcde","*a?c*"))