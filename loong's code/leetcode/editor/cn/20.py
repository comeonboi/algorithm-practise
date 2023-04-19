class Solution:
    def isValid(self, s: str) -> bool:
        stack = ["?"]
        dic = {'{': '}', '[': ']', '(': ')', '?': '?'}
        for i in s:
            if i in dic:
                stack.append(i)
            elif dic[stack.pop()] != i:
                return False
        return len(stack) == 1


print(Solution.isValid(Solution(), s="()[]{}"))
