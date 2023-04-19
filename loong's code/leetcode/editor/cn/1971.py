from collections import defaultdict

import numpy
import networkx as nx
import matplotlib.pyplot as plt


class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        def recursion(current_doll):
            if current_doll == destination:
                return True
            vis.add(current_doll)
            flag = 0
            for j in matrix[current_doll]:
                if j > 0 and flag not in vis and recursion(flag):
                    return True
                flag += 1
            return False

        vis = set()
        matrix = numpy.zeros([n, n], dtype=int)
        for i in edges:
            x, y = tuple(i)
            matrix[x][y] = 1
            matrix[y][x] = 1
        g = defaultdict(list)
        # print(matrix)
        # G = nx.from_numpy_matrix(matrix, parallel_edges=True, create_using=nx.MultiGraph)
        # nx.draw(G)
        # plt.show()
        return recursion(source)


print(Solution.validPath(Solution, n=3, edges=[[0, 1], [1, 2], [2, 0]], source=0, destination=2))
