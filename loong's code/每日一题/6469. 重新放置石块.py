from typing import List


class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        ans = []
        num_mod = []

        for i, j in zip(moveFrom, moveTo):
            if i in nums or i in num_mod:


                ans.append(j)
                if i in ans:
                    while i in ans:
                        ans.remove(i)
                num_mod.append(j)
                if i in nums:
                    while i in nums:
                        nums.remove(i)


            print(ans, nums, num_mod)
        ans.extend(nums)
        return sorted(list(set(ans)))


from collections import defaultdict

# class Solution:
#     def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
#         # 创建哈希表记录数字的最新位置
#         # position = defaultdict(int)
#         # for i in range(len(moveFrom)):
#         #     position[moveFrom[i]] = moveTo[i]
#         position = dict(zip(moveFrom, moveTo))
#         # 根据哈希表更新nums列表中的数字
#         for i in range(len(moveFrom)):
#             if moveFrom[i] in nums:
#                 nums[nums.index(moveFrom[i])] = position[moveFrom[i]]
#                 # print(nums)
#
#         # 返回去重后的排序列表
#         return sorted(list(set(nums)))


print(Solution().relocateMarbles(nums=[3, 4], moveFrom=[4, 3, 1, 2, 2, 3, 2, 4, 1], moveTo=[4, 3, 1, 2, 2, 3, 2, 4, 1]))
