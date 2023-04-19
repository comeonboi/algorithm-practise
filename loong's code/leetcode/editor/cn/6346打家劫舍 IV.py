from typing import List
class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            for j in range(i+2,len(nums)):

