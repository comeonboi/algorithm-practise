class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        result = 0
        g.sort()
        s.sort()
        gi = len(g)-1
        si = len(s)-1
        while gi >=0 and si >=0:
            if s[si] >= g[gi]:
                result += 1
                gi-=1
                si-=1
            else:
                gi-=1
        return result
