from typing import List
class Solution:
    def distinctIntegers(self, n: int) -> int:
        ans = set()
        for i in range(n, 1, -1):
            for j in range(2, i):
                if i % j == 1:
                    ans.add(j)
        return len(ans) + 1
print(Solution.distinctIntegers(Solution,n=5))