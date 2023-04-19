from typing import List


class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        return all((v != 0) == (i == j or i + j == len(grid) - 1) for i, row in enumerate(grid) for j, v in enumerate(row))
