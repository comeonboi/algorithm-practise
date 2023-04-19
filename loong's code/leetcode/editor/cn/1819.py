from math import gcd
from typing import List


class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        ans, mx = 0, max(nums)
        has = [False] * (mx + 1)
        for x in nums:
            # 只更新数组中存在的数
            has[x] = True
        for i in range(1, mx + 1):
            g = 0  # 0 和任何数 x 的最大公约数都是 x
            for j in range(i, mx + 1, i):  # 枚举 i 的倍数 j
                if has[j]:  # 如果 j 在 nums 中
                    g = gcd(g, j)  # 更新最大公约数
                    if g == i:  # 找到一个答案（g 无法继续减小）
                        ans += 1
                        break  # 提前退出循环
        return ans

        # 调和级数部分和
