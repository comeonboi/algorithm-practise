from bisect import bisect_right
from itertools import accumulate
from typing import List


class Solution:

    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        # nums = sorted(nums)
        # #创建一个长度位queries的数组
        # ans = [0] * len(queries)
        # for i in queries:
        #     # 维护最长子序列
        #     ans_1 = 0
        #     for left, j in enumerate(nums):
        #         right = len(nums) - 1
        #         while sum(nums[left:right + 1]) > i:
        #             right -= 1
        #             # if sum(nums[left:right + 1]) <= i:
        #             #     break
        #             if right < left:
        #                 break
        #         ans_1 = max(ans_1, right - left + 1)
        #         ans[queries.index(i)] = ans_1
        # return ans
        nums.sort()
        s = list(accumulate(nums))
        ans = []
        for q in queries:
            ans.append(bisect_right(s, q))
        return ans
print(Solution.answerQueries(Solution(), nums = [4,5,2,1], queries = [3,10,21]))