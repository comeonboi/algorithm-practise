import numpy as np


class Solution:
    def isPossible(self, n: int, edges: list[list[int]]) -> bool:
        matrix = np.zeros([n, n], dtype=int)
        for i in edges:
            x, y = tuple(i)
            matrix[x - 1][y - 1] = 1
            matrix[y - 1][x - 1] = 1
        row, col = np.diag_indices_from(matrix)
        matrix[row, col] = 2
        odd_list = []
        for i in range(n):
            if list(matrix[i]).count(1) % 2 != 0:
                odd_list.append(i)
        print(matrix)
        if len(odd_list) / 2 <= 2:
            return True
        else:
            return False

print(Solution.isPossible(Solution, n = 4, edges = [[1,2],[1,3],[1,4]]))
