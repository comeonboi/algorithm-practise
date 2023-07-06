class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        self.back_tracking(k,n,1,[],result)
        return result
    def back_tracking(self,k,n,start_index,path,result):
        if len(path) == k and sum(path)==n:
            result.append(path[:])
            return
        if len(path) == k and sum(path)!=n:
            return
        for i in range(start_index,9-(k-len(path))+2):
            path.append(i)
            self.back_tracking(k, n, i+1, path, result)
            path.pop()