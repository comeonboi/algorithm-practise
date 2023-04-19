import math
from typing import List


class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        print(math.gcd(*nums))
        return True if math.gcd(*nums) == 1 else False

print(Solution.isGoodArray(Solution(), nums = [12,5,7,23]))