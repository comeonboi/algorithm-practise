def threeSum(self, nums: List[int]) -> List[List[int]]:
    # ctr = Counter(a + b for a in nums for b in nums)
    # for i in nums:
    #     del ctr[i * 2]
    # for i in nums:
    #     for j in nums:
    #         for k in nums:
    ans = []
    n = len(nums)
    if len(nums) < 3:
        return ans
    nums.sort()
    for i in range(n - 2):
        if nums[i] + nums[i + 1] + nums[i + 2] > 0:
            break
        if nums[i] + nums[n - 2] + nums[n - 1] < 0:
            continue
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        s, q = i + 1, n - 1
        while s < q:
            sum = nums[i] + nums[s] + nums[q]
            if sum == 0:
                ans.append([nums[i], nums[s], nums[q]])
                while s < q and nums[s] == nums[s + 1]:
                    s += 1
                while s < q and nums[q] == nums[q - 1]:
                    q -= 1
                s += 1
                q -= 1
            elif sum < 0:
                s += 1

            else:
                q -= 1
    return ans