class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = ""
        for i in range(len(s)):
            if stack == "":
                stack += s[i]
            else:
                if stack[-1] == s[i]:
                    stack = stack[:-1]
                else:
                    stack += s[i]
        return stack