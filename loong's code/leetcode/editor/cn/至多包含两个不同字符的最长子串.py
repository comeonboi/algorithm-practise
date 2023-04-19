class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        """ 如果窗口中的元素《= 2 窗口右滑
        如果窗口中的元素》2，窗口左滑
        """
        hash_1 = {}
        n = len(s)
        o_res = 0
        left = right = 0
        while right < n:
            x = set(s[left:right + 1])
            if len(set(s[left:right + 1])) <= 2:
                right += 1
            else:
                hash_1[right - left] = right - left
                left += 1
        else:
            hash_1[right - left] = right - left
        return hash_1[max(hash_1.keys())]


print(Solution.lengthOfLongestSubstringTwoDistinct(Solution(), s="ccaabbb"))
