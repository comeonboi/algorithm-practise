from typing import List


class Solution:
    def countAsterisks(self, s: str) -> int:
        stack = True
        flag = 0
        for i in s:
            if stack:
                if i == '*':
                    flag += 1
            if i == '|' and stack:
                stack = False
            elif i == '|' and not stack:
                stack = True
        return flag

class Solution:
    def countAsterisks(self, s: str) -> int:
        count1, count2 = 0, 0
        for i in range(len(s)):
            if s[i] == '|':
                count1 += 1
            if count1 % 2 == 0 and s[i] == '*':
                count2 += 1
        return count2
print(Solution.countAsterisks(Solution(), s="l|*e*et|c**o|*de|"))
