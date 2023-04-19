from typing import List
from collections import defaultdict, Counter


class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        # 先判断 FlushCounter(suits)
        dict1 = Counter(suits)
        dict2 = Counter(ranks)
        if len(dict1) == 1:
            return "Flush"
        # 判断三条
        if any(dict2[i]>=3 for i in dict2):
            return "Three of a Kind"
        # 判断对子
        if any(dict2[i]==2 for i in dict2):
            return "Pair"
        return "High Card"
