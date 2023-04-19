from typing import List


class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        LIM = 512
        R, C = len(matrix), len(matrix[0])
        res = [[0] * C for _ in range(R)]
        countR, countC = [0] * R, [0] * C

        # 按元素大小分别存储元素坐标
        ls = collections.defaultdict(list)
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                ls[val].append((r, c))

        # 并查集用于合并行或列相同的元素
        union = list(range(LIM * 2))

        def find(i):
            if union[i] == i: return i
            union[i] = find(union[i])
            return union[i]

        # 按val从小到大遍历
        pool = collections.defaultdict(list)
        for val in sorted(ls.keys()):

            # 用并查集合并行和列相同的元素并分组
            for r, c in ls[val]:
                union[find(r)] = find(c + LIM)
            pool.clear()
            for r, c in ls[val]:
                pool[find(r)].append((r, c))

            # 行和列相同的元素，共享相同的rank
            for group in pool.values():
                rank = max(max((countR[r], countC[c])) for r, c in group) + 1
                for r, c in group:
                    countR[r] = countC[c] = res[r][c] = rank
                    # 重置并查集
                    union[r] = r
                    union[c + LIM] = c + LIM
        return res
