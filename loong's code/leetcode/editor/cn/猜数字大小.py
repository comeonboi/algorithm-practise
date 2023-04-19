# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:
def guess(num: int, pick=6) -> int:
    if num < pick:
        return 1
    if num > pick:
        return -1
    else:
        return 0


class Solution:
    def guessNumber(self, n: int) -> int:
        def recursion(nums, left, right):
            if left > right:
                # 递归结束
                return -1
            mid = left + (right - left) // 2
            if guess(mid) == 0:
                return mid
            elif guess(mid) == 1:
                left = mid + 1
            else:
                right = mid - 1
            return recursion(nums, left, right)

        left = 1
        right = n
        return recursion(n, left, right)

print(Solution.guessNumber(Solution,n = 6))