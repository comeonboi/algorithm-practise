class Solution:
    def countEven(self, num: int) -> int:
        y, x = divmod(num, 10)
        ans = y * 5
        y_sum = 0
        while y:
            y_sum += y % 10
            y //= 10
        return ans + ((x + 1) // 2 - 1 if y_sum % 2 else x // 2)

print(Solution.countEven(Solution(),num=300))