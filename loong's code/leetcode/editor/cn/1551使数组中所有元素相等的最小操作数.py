class Solution:
    def minOperations(self, n: int) -> int:
        operate = 0
        for i in range(1, n, 2):
            operate += (n - i)
        return operate


print(Solution.minOperations(Solution(), n=6))
