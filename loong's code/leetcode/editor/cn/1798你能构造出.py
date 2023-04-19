from typing import List
class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        m = 0  # 一开始只能构造出 0
        coins.sort()
        for c in coins:
            if c > m + 1:  # coins 已排序，后面没有比 c 更小的数了
                break  # 无法构造出 m+1，继续循环没有意义
            m += c  # 可以构造出区间 [0,m+c] 中的所有整数
        return m + 1  # [0,m] 中一共有 m+1 个整数

print(Solution.getMaximumConsecutive(Solution,coins=[1,2,3,4]))