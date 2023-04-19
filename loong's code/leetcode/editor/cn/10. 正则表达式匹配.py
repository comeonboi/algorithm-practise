class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # 传入 a* a aa aaa aaaa
        # a*b ab aab aaab aaaaab

        m, n = len(s), len(p)
        #
        # 状态定义 定义 `dp[i][j]` 表示 s 的前 i 个字符和 p 的前 j 个字符能否匹配。

        dp = [[False] * (n+1) for _ in range(m+1)]
        # p[j]= '.'，则 p[j]p[j]p[j] 一定可以与 s[i]s[i]s[i] 匹配成功，此时有 dp[i][j]=dp[i−1][j−1]