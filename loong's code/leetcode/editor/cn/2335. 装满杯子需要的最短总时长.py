from typing import List


class Solution:
    def fillCups(self, amount: List[int]) -> int:
        amount.sort()
        count = 0
        # 尽量避免归0
        while amount[-1] > 0:
            if amount[-1] > 0 and amount[1] > 0:
                amount[-1] -= 1
                amount[1] -= 1
                count += 1
            if amount[-1] > 0 and amount[1] == 0:
                return count + amount[-1]
            amount.sort()
        return count



print(Solution.fillCups(Solution(), amount=[0,2,2]))
