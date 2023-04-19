from typing import List


class Solution:
    def captureForts(self, forts: List[int]) -> int:
        n = len(forts)
        i, L = 0, None
        ans = 0
        while i < n:
            #对于每一个1或者-1，找离他最近的相反数，计算距离，更新答案
            if forts[i] == 1 or forts[i] == -1:
                if L is not None and forts[i] == -forts[L]:
                    ans = max(ans, i - L - 1)
                L = i
            i += 1
        return ans

print(Solution.captureForts(Solution(),forts = [-1,0,-1,0,1,1,1,-1,-1,-1]))
