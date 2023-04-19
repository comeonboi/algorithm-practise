class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        low, high = 0, len(numbers) - 1
        while low < high:
            total = numbers[low] + numbers[high]
            if total == target:
                return [low + 1, high + 1]
            elif total < target:
                low += 1
            else:
                high -= 1

        return [-1, -1]


print(Solution.twoSum(Solution, numbers = [2,7,11,15], target = 9))
