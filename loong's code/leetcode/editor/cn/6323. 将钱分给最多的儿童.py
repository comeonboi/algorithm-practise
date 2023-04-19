
from typing import List


class Solution:
    def distMoney(self, money: int, children: int) -> int:
        money -= children
        children_list = [1] * children
        if money < 0:
            return -1
        counts = min(money // 7, children)
        for i in range(counts):
            children_list[i] = 8
        children_list[-1] += money - counts * 7
        counts = children_list.count(8)
        if children_list[-1] == 4:
            if children_list[-2] != 8:
                pass
            else:
                counts -= 1
        return counts


print(Solution().distMoney(23, 2))
