from typing import List
class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        def put_jewels_in_bags(weights, k):
            def dfs(start, k, score):
                nonlocal max_score, min_score
                if k == 1:
                    max_score = max(max_score, score + weights[start] + weights[-1])
                    min_score = min(min_score, score + weights[start] + weights[-1])
                    return
                for i in range(start, len(weights) - k + 1):
                    dfs(i + 1, k - 1, score + weights[start] + weights[i])

            max_score, min_score = float('-inf'), float('inf')
            dfs(0, k, 0)
            return max_score - min_score
