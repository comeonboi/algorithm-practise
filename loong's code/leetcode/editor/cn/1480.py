def runningSum(nums: list[int]) -> list[int]:
    length = len(nums)
    for i in range(length):
        if i + 1 < length:
            nums[i+1] += nums[i]
    return nums


class Solution:
    num = []
    while 1:
        x = input()
        if x.isdigit():
            num.append(int(x))
        else:
            break
    runningSum(num)
