from typing import List


class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2:
            return []
        res = []
        total = 0
        #Greedy
        for i in range(2, finalSum + 1, 2):
            res.append(i)
            total += i
            if total >= finalSum:
                break
        if total == finalSum:
            return res
        else:
            temp = total - finalSum
            res.pop(res.index(temp))
        return res