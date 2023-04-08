class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        j = 0
        result = []
        for i in range(len(nums)):
            if i == 0:
                continue
            else:
                if abs(nums[i]) <= abs(nums[j]):
                    j = i
                else:
                    break
        result.append(nums[j] ** 2)
        left = j - 1
        right = j + 1
        while (left >= 0 and right <= (len(nums) - 1)):
            if abs(nums[left]) <= abs(nums[right]):
                result.append(nums[left] ** 2)
                left -= 1
            else:
                result.append(nums[right] ** 2)
                right += 1
        while (left >= 0):
            result.append(nums[left] ** 2)
            left -= 1
        while (right <= (len(nums) - 1)):
            result.append(nums[right] ** 2)
            right += 1
        return result
