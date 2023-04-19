from typing import List


class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        flag = 0
        for i in range(len(nums)):
            temp_nums = nums[:i] + nums[i+1:]
            if sum(temp_nums[::2])==sum(temp_nums[1::2]):
                flag += 1
        return flag



print(Solution.waysToMakeFair(Solution(),nums = [2,1,6,4]))
#不失一般性，现在我们将下标 iii 的元素进行删除，
# 显而易见下标 iii 之前的元素下标并不会因此发生改变，
# 而下标 iii 之后的原本在 jjj，j>ij > ij>i
# 下标的数组元素会移动到下标 j−1，即下标 iii
# 之后的奇数下标元素会成为偶数下标元素，偶数下标元素会成为奇数下标元素。
class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        res = odd1 = even1 = odd2 = even2 = 0
        for i, num in enumerate(nums):
            if i & 1:
                odd2 += num
            else:
                even2 += num
        for i, num in enumerate(nums):
            if i & 1:
                odd2 -= num
            else:
                even2 -= num
            if odd1 + even2 == odd2 + even1:
                res += 1
            if i & 1:
                odd1 += num
            else:
                even1 += num
        return res