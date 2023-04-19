import re
from typing import List


class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        b = re.findall(r'[(](.*?)[)]', s)
        knowledge = dict(knowledge)
        for i in b:
            new_str = '('+i+')'
            if i in knowledge:
                s = s.replace(new_str, knowledge[i])
            else:
                s = s.replace(new_str, "?")
        return s

print(Solution.evaluate(Solution(),s = "hi(name)", knowledge = [["a","b"]]))