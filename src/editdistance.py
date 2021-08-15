def editdistance(str1: str, str2: str):
    n, m = len(str1), len(str2)
    dp = [[0]*(m+1) for _ in range(n+1)]

    for i in range(n+1):
        dp[i][0] = i
    for i in range(m+1):
        dp[0][i] = i

    for i in range(1, n+1):
        for j in range(1, m+1):
            cost = 0 if str1[i-1] == str2[j-1] else 1
            dp[i][j] = min(dp[i-1][j]+1,  # insertion
                           dp[i][j-1] + 1,  # deletion
                           dp[i-1][j-1]+cost)  # replacement

    return dp[n][m]


n, m = map(str, input().split())
print(editdistance(n, m))
