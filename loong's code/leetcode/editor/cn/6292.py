from typing import List

import numpy as np


class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        matrix = np.zeros((n, n), dtype = int)
        for row1, col1, row2, col2 in queries:
            matrix[row1:row2+1, col1:col2 + 1] += 1
        return matrix.tolist()
        print(matrix)


print(Solution.rangeAddQueries(Solution(), n = 13, queries = [[3,1,7,3],[7,5,7,8],[4,12,6,12],[2,8,6,11],[9,11,10,11],[9,3,11,11],[0,12,10,12],[10,5,11,12],[4,7,6,12],[0,2,9,6],[12,7,12,11],[2,7,3,8],[2,9,6,12],[10,7,10,12],[11,6,11,7],[3,2,12,9]]))