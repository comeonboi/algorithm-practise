def climbStairs(self, n: int) -> int:
    # 动态规划
    dp = [1, 1]
    for i in range(2, n + 1):
        dp.append(0)
    i = 2
    while i < n + 1:
        dp[i] = dp[i - 1] + dp[i - 2]
        i += 1
    return dp[n]
    # 递归
    # 究极超时
    # if n == 0 or n == 1:
    #     return 1
    # else:
    #     return self.climbStairs(n - 1) + self.climbStairs(n - 2)