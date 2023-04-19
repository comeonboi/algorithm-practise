from typing import List
n, k = map(int, input().split())
a = [0] + list(map(int, input().split()))

dp = [[0] * (k+1) for _ in range(n+1)]
for i in range(1, n+1):
    dp[i][0] = dp[i-1][0] + a[i]

for i in range(2, n+1):
    for j in range(1, k+1):
        dp[i][j] = max(dp[i-1][j], dp[i-2][j-1] + a[i])

print(dp[n][k] - 3)
