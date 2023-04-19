from typing import List


class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        flag = 0
        for i in patterns:
            if i in word:
                flag += 1
        return flag


print(Solution.numOfStrings(Solution, patterns=["a", "b", "c"], word="aaaaabbbbb"))
