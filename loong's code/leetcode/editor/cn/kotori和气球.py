# n种气球，一排m个气球
import math


def count_permutations(n: int, m: int) -> int:
    MOD = 109  # 取模的值

    cnt = n
    for i in range(0, m - 1):
        cnt *= (n - 1)
        cnt = cnt % MOD
    return cnt % MOD


n, m = map(int, input().split())
result = count_permutations(n, m)
print(result)