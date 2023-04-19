from typing import List
import collections

class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        print((set(nums1) & set(nums2)) |(set(nums1) & set(nums3)) |(set(nums2) & set(nums3)))
        print((set(nums1) & set(nums3))|(set(nums2) & set(nums3)))
        return list(
            (set(nums1) & set(nums2)) |
            (set(nums1) & set(nums3)) |
            (set(nums2) & set(nums3))
        )

print(Solution.twoOutOfThree(Solution(), nums1 = [1,1,3,2], nums2 = [2,3], nums3 = [3]))