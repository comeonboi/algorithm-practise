from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix) - 1, -1, -1):
            for j in range(len(matrix)):
                matrix[j].append(matrix[i][0])
                del (matrix[i][0])

