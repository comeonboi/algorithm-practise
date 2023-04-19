class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        nums = set()
        for i in range(1, 2 ** p):
            nums.add(bin(i)[2:])
        return nums


print(Solution.minNonZeroProduct(Solution(), p=2))
