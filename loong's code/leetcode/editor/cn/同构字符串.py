from itertools import groupby


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash_map = {}
        value = set()
        for i in range(len(s)):
            if s[i] in hash_map:
                if hash_map[s[i]] != t[i]:
                    return False
            else:
                if t[i] in value:
                    return False
                hash_map[s[i]] = t[i]
                value.add(t[i])
        return True


print(Solution.isIsomorphic(Solution(), s = "badc", t = "baba"))