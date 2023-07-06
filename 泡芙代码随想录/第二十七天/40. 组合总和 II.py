class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        self.back_tracking(candidates, target, 0, [], result)
        return result

    def back_tracking(self, candidates, target, start_index, path, result):
        if target == 0:
            result.append(path[:])
            return

        for i in range(start_index, len(candidates)):
            if candidates[i] > target:
                return
            if i > start_index and candidates[i] == candidates[i - 1]:
                continue
            path.append(candidates[i])
            self.back_tracking(candidates, target - candidates[i], i + 1, path, result)
            path.pop()