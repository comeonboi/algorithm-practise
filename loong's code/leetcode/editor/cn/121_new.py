class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        maxMon = 0
        minprice = prices[0]
        for i in range(len(prices)):
            # 边遍历边寻找最小值
            minprice = min(minprice, prices[i])
            # 一个在最前面找最低点，一个在后面判断卖不卖
            maxMon = max(maxMon, prices[i] - minprice)
        return maxMon

print(Solution.maxProfit(Solution, prices=[7, 6, 4, 3, 1]))
