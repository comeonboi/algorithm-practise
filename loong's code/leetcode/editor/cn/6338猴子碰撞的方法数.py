from typing import List


class Solution:
    def countAliveMonkeys(self, n: int) -> int:
        mod = 10 ** 9 + 7
        res = 1
        x = 2
        while n > 0:
            if n % 2 == 1:
                res = (res * x) % mod
            x = (x * x) % mod
            n = n // 2
        return (res - 2) % mod

# 此程序使用快速幂算法来降低计算 2^n 的时间复杂度。在这里，我们用变量 x 来存储 2^n，并在每次循环中将 x 平方。当 n 为奇数时，我们将结果乘以 x。这样可以在每次循环中计算出2^n。
#
# 在返回结果之前，我们需要用(res-2)%mod 去除边界情况。
print(Solution.countAliveMonkeys(Solution(), n=5))


def monkey_collision(n: int) -> int:
    if n == 1:
        return 0
    if n == 2:
        return 2
    f = [0, 2]
    for i in range(2, n):
        f.append((i - 1) * f[i - 1] + (i - 1) * (i - 2))
    return f[n - 1]


print(monkey_collision(n=3))
