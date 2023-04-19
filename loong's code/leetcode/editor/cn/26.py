class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        a = set(nums)  # 变成集合
        nums.clear()  # 清空列表
        a = list(a)  # 集合变列表
        nums.extend(a)  # 将集合添加到列表
        nums.sort()
        return len(nums)


print(Solution.removeDuplicates(Solution(), nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
