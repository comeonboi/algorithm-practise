from typing import List
# 求上升区间的高度和

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        for i in range(len(prices)-1):
            # 非常好的一个判断正负的方法，学到了
            total += max(prices[i+1]-prices[i], 0)
        return total

print(Solution.maxProfit(Solution(), prices=[7, 1, 5, 3, 6, 4]))
