class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        maxNum = 0
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                maxNum = max(maxNum, prices[j] - prices[i])
        return maxNum


print(Solution.maxProfit(Solution, prices=[7, 6, 4, 3, 1]))
