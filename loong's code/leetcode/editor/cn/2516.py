class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        hash_dict = {'a':0, 'b':0, 'c':0}
        start = 0
        tail = len(s) - 1
        while 1:
            hash_dict[s[start]] += 1
            if hash_dict[s[start]] >= k:
                tail -= 1
                hash_dict[s[tail]] += 1
            if hash_dict['a'] >=k and hash_dict['b'] >= k and hash_dict['c'] >= k:
                return hash_dict['a']+hash_dict['b']+hash_dict['c']
            if start == tail:
                return -1
            start += 1


print(Solution.takeCharacters(Solution(), s = "aabaaaacaabc", k = 2))



