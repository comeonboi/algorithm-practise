import collections
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_1 = {}
        hash_2 = {}
        for index, i in enumerate(nums):
            if i not in hash_1:
                hash_1[i] = 1
                hash_2[i] = [index]
            else:
                hash_1[i] += 1
                hash_2[i].append(index)
        for i in hash_1:
            if hash_1[i] >= 2:
                for j in range(len(hash_2[i])):
                    for m in range(j + 1, len(hash_2[i])):
                        if abs(hash_2[i][j] - hash_2[i][m]) <= k:
                            return True
        return False


print(Solution.containsNearbyDuplicate(Solution(), nums=[1, 0, 1, 1], k=1))


# 整理题意：是否存在长度不超过的 k+1k + 1k+1 窗口，窗口内有相同元素。
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        s = set()
        for i in range(n):
            if i > k:
                s.remove(nums[i - k - 1])
            if nums[i] in s:
                return True
            s.add(nums[i])
        return False


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1 = collections.Counter(nums1)
        num2 = collections.Counter(nums2)
        num = num1 & num2
        return num.elements()
