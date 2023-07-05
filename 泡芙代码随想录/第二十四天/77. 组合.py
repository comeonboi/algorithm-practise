class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        self.backtracking(n,k,1,[],result)
        return result

    def backtracking(self,n,k,start_index,path,result):
        if len(path)==k:
            result.append(path[:])
            return
        for i in range(start_index,n-(k-len(path))+2):
            path.append(i)
            self.backtracking(n, k, i+1, path, result)
            path.pop()