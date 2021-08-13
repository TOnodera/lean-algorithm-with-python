def chmin(a:int,b:int):
    if a>b:
        a = b
    return a


INF = 1 << 60

N = int(input())
h = []
for i in range(N):
    h.append(int(input()))

dp=[INF for i in range(N)]
dp[0] = 0

for i in range(N):
    dp[i] = chmin(dp[i],dp[i-1]+abs(h[i]-h[i-1]))
    if(i>1):
        dp[i] = chmin(dp[i],dp[i-2]+abs(h[i]-h[i-2]))

print(dp[N-1])
