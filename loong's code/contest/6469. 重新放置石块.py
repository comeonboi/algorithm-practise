from typing import List


class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        ans = []
        num_mod = []

        for i, j in zip(moveFrom, moveTo):
            if i in nums or i in num_mod:
                ans.append(j)
                if i in ans and i != j:
                    while i in ans:
                        ans.remove(i)
                num_mod.append(j)
                if i in nums and i != j:
                    while i in nums:
                        nums.remove(i)
            print(ans, nums, num_mod)
        ans.extend(nums)
        return sorted(list(set(ans)))

class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        ans = set(nums)
        num_mod = set()

        for i, j in zip(moveFrom, moveTo):
            if i in ans or i in num_mod:
                ans.add(j)
                if i != j:
                    ans.discard(i)
                num_mod.add(j)
                nums = [x for x in nums if x != i]

        ans.update(nums)
        return sorted(ans)
class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        mapping = dict(zip(moveFrom, moveTo))
        ans = []

        for num in nums:
            if num in mapping:
                ans.append(mapping[num])

        return sorted(ans)

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


print(Solution().relocateMarbles(nums = [1,6,7,8], moveFrom = [1,7,2], moveTo = [2,9,5]))
