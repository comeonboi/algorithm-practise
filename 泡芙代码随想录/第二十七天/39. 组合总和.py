class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.back_tracking(candidates, target,[],result)
        return result
    def back_tracking(self, candidates, target ,path, result):
        if sum(path) == target and sorted(path) not in result:
            result.append(sorted(path[:]))
            return
        if sum(path) > target:
            return
        for i in range(len(candidates)):
            path.append(candidates[i])
            self.back_tracking(candidates, target, path, result)
            path.pop()
