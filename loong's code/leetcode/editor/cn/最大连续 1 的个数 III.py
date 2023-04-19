from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        k_mean = k
        # 用于记录现在有多少子数组
        flag = 0
        # 用于记录最大地子数组
        max_flag = 0
        for start in range(len(nums)):
            tail = start
            while k >= 0:
                if nums[tail] == 1:
                    tail += 1
                    flag += 1
                elif nums[tail] == 0 and k > 0:
                    tail += 1
                    k -= 1
                    flag += 1
                elif nums[tail] == 0 and k == 0:
                    k = k_mean
                    max_flag = max(max_flag, flag)
                    flag = 0
                    break
                if tail == len(nums):
                    max_flag = max(max_flag, flag)
                    flag = 0
                    break
        return max_flag
print(Solution.longestOnes(Solution(), nums = [0,0,0,1], k = 3))

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        思路：1. k=0可以理解为求最长重复子串问题
             2. 如果当前窗口值-窗口中1的个数 <= k: 则扩大窗口(right+1)
                如果当前窗口值-窗口中1的个数 > k: 则向右滑动窗口(left+1)
        方法：哈希表 + 滑动窗口
        """
        n = len(nums)
        o_res = 0
        left = right = 0
        while right < n:
            if nums[right]== 1:
                o_res += 1
            if right-left+1- o_res > k:
                if nums[left]== 1:
                    o_res -= 1
                left += 1
            right += 1
        return right - left
#
# 作者：Lincoln
# 链接：https://leetcode.cn/leetbook/read/hash-table-plus/x72767/?discussion=cSlL17
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。