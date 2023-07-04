def matrixSum(self, nums: List[List[int]]) -> int:
    ans = 0
    while len(nums[0]):
        score = 0
        for num in nums:
            n = max(num)
            num.pop(num.index(n))
            score = max(score, n)
        ans += score
    return ans