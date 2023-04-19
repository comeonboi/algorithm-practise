from collections import Counter


class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        asq = Counter(s)
        asq2 = Counter(target)

        res = float('inf')
        for ch, cnt in asq2.items():
            if asq[ch] // cnt < res:
                res = asq[ch] // cnt
        return res


print(Solution.rearrangeCharacters(Solution, s="abbaccaddaeea", target="aaaaa"))
