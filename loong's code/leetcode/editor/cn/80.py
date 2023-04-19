from collections import Counter
from typing import List


class Solution:
    def removeDuplicates(self, nums: list[int]) -> list[int]:
        dict1 = Counter(nums)
        for i in dict1:
            if dict1[i] > 2:
                dict1[i] = 2
        list1 = list(dict1.elements())
        nums = list1
        return nums


print(Solution.removeDuplicates(Solution(), nums=[1, 1, 1, 2, 2, 3]))
