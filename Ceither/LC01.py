def twoSum(self, nums: List[int], target: int) -> List[int]:
    hash_table = {}
    for i in range(len(nums)):
        if hash_table.get(target - nums[i]) is not None:
            return [hash_table.get(target - nums[i]), i]
        hash_table[nums[i]] = i