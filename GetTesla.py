def getTesla(m):
    row = len(m)
    column = len(m[0])

    dp = [[float('inf') for x in range(column)] for y in range(row)]


    for i in range(row - 1, -1, -1):
        for j in range(column - 1, -1, -1):
            if i == row -1 and j == column - 1:
                dp[i][j] = max(1, 1 - m[row - 1][column - 1])
            elif i == row - 1:
                dp[i][j] = max(1, (dp[i][j+1] - m[i][j]))
            elif j == column -1:
                dp[i][j] = max(1, (dp[i+1][j] - m[i][j]))
            else:
                dp[i][j] = max(1,min(dp[i + 1][j], dp[i][j + 1])-m[i][j])

    return dp[0][0]

M = [[-1, -2, 2], [10, -8, 1], [-5, -2, -3]]
dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
x = [[0]]
print(getTesla(x))