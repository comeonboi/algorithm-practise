from typing import List


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        ans = []
        for i in range(len(grid) - 2):
            for j in range(len(grid) - 2):
                print(grid[i:2 + i][j:2 + j])
                ans.append(max(grid[i:2 + i][j:2 + i]))
        return ans


print(Solution.largestLocal(Solution(), [[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]]))
