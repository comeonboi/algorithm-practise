import collections
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #     return False
        # hash_table = {}
        # for i in s:
        #     if hash_table.get(i):
        #         hash_table[i] += 1
        #     else:
        #         hash_table[i] = 1
        # for i in t:
        #     if hash_table.get(i):
        #         hash_table[i] -= 1
        #     else:
        #         return False
        # return True
        return Counter(s) == Counter(t) #真得一行吧