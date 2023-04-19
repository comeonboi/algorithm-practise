import re
from typing import List

#此函数首先使用列表推导式计算每个元素之间的差异。然后，它初始化一个计数器以跟踪所需的操作数。接下来，它遍历差异，并检查每个差异是否可以被 整除。如果不是，则返回 -1，因为数组不能与给定的操作相等。如果它是可整除的，它将差值的绝对值除以添加到计数器中。最后，它返回所需的操作数。nums1nums2operationskkoperations
class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        if k <= 0:
            if nums1 != nums2:
                return -1
            else:
                return 0
        diff = [nums1[i] - nums2[i] for i in range(len(nums1))]
        if sum(diff) != 0:
            return -1
        if sum(diff) % k != 0:
            return -1
        operations = 0
        for index, d in enumerate(diff):
            if d % k != 0:
                return -1
            if d > 0:
                operations += d // k
        return operations


print(Solution.minOperations(Solution(), nums1=[0, 0, 0, 0], nums2=[0, 0, 0, 0], k=1))
