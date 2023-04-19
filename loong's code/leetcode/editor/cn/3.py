class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = []
        ans1 = []
        flag = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[j] not in ans:
                    ans.append(s[j])
                else:
                    ans1.append(ans)
                    ans = []
                    break
        else:
            ans1.append(ans)
        for i in ans1:
            flag = max(flag, len(i))
        return flag


print(Solution.lengthOfLongestSubstring(Solution(), s="asjrgapa"))
