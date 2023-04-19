from collections import defaultdict


class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        def dfs(i):
            if i == destination:
                return True
            vis.add(i)
            for j in g[i]:
                if j not in vis and dfs(j):
                    return True
            return False

        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        print(g)
        vis = set()
        return dfs(source)

print(Solution.validPath(Solution, n=3, edges=[[0, 1], [1, 2], [2, 0]], source=0, destination=2))
