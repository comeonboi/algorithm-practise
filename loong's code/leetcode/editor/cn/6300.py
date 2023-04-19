from typing import List


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        common = set(nums1).intersection(nums2)
        if common:
            return min(common)
        return -1
