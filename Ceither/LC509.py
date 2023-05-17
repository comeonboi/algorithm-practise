#动态规划
def fib(self, n: int) -> int:
    dp = [0, 1]
    for i in range(2, n + 1):
        dp.append(0)
    i = 2
    while 2 <= i < n + 1:
        dp[i] = dp[i - 1] + dp[i - 2]
        i += 1
    return dp[n]