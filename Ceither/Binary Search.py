def binarysearch(nums, target):
    id = len(nums) // 2
    if nums[id] == target:
        return id
    elif nums[id] > target:
        return binarysearch(nums[:id], target)
    else:
        return binarysearch(nums[id+1:], target)
