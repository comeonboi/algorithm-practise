class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        start = 0
        max_len = 0
        lookup = set()
        flag = 0
        for i in range(len(s)):
            flag += 1
            while s[i] in lookup:
                lookup.remove(s[start])
                start += 1
                flag -= 1
            if flag > max_len:
                max_len = flag
            lookup.add(s[i])
        return max_len


print(Solution.lengthOfLongestSubstring(Solution(), s="abcbbcbb"))
