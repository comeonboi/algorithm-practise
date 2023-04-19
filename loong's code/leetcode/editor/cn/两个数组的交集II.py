from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for i in nums1:
            if i in nums2:
                ans.append(i)
                nums2.remove(i)
        return ans


print(Solution.intersect(Solution, nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4]))
