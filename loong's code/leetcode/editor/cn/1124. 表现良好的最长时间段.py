from functools import cache
from typing import List


class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        ans = 0
        for index, i in enumerate(hours):
            count = 0
            j = index
            while j < len(hours):
                if hours[j] <= 8:
                    count -= 1
                elif hours[j] > 8:
                    count += 1
                if count > 0:
                    ans = max(ans, j - index + 1)
                j += 1
        return ans


class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        n = len(hours)
        s = [0] * (n + 1)
        st = [0]
        for j, h in enumerate(hours, 1):
            s[j] = s[j - 1] + (1 if h > 8 else -1)
            if s[j] < s[st[-1]]:
                st.append(j)
        ans = 0
        for i in range(n, 0 , -1):
            while st and s[i] > s[st[-1]]:
                ans = max(ans, i-st.pop())
        return ans


print(Solution.longestWPI(Solution(), hours=[9, 9, 6, 0, 6, 6, 9]))
