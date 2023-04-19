import copy
from itertools import accumulate
from typing import List

class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        matrix_heng = copy.deepcopy(grid)
        matrix_su = copy.deepcopy(grid)
        for ind, i in enumerate(grid):
            for index in range(len(i)):
                # 每一行相加
                if index >= 1:
                    matrix_heng[ind][index] += matrix_heng[ind][index-1]
                # 每一列相加
                if ind >= 1:
                    matrix_su[ind][index] += matrix_su[ind-1][index]
        m, n = len(grid), len(grid[0])
        # rs = [list(accumulate(row, initial=0)) for row in grid]  # 每行的前缀和
        # cs = [list(accumulate(col, initial=0)) for col in zip(*grid)]  # 每列的前缀和
        print(matrix_heng, matrix_su)
        # d 是最大面积
        for d in range(min(m,n), 0, -1):
            for i in range(m-d+1):
                for j in range(n-d+1):
                    if matrix_heng[i][j+d] - matrix_heng[i][j] == d and\
                        matrix_heng[i+d-1][j+d] - matrix_heng[i+d-1][j] == d and\
                        matrix_su[j][i+d] - matrix_su[j][i] == d and\
                        matrix_su[j+d-1][i+d] - matrix_su[j+d-1][i] == d:
                        return d**2
        return 0


print(Solution.largest1BorderedSquare(Solution(), grid = [[1,1,1],[1,0,1],[1,1,1]]))