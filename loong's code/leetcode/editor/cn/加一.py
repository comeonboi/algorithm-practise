from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits=[str(i) for i in digits]
        digits = int(''.join(digits))
        digits += 1
        # digits = str(digits).split()
        digits = list(str(digits))
        digits = [int(i) for i in digits]
        return digits


print(Solution.plusOne(Solution(), digits=[9]))
