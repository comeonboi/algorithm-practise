from typing import List

class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        if income == 0:
            return 0
        tax: float = 0
        index: int = 1
        if income < brackets[0][0]:
            return income * brackets[0][1] / 100
        else:
            tax += brackets[0][0] * brackets[0][1] / 100
        while index < len(brackets):
            # 判断是不是在最后一位了
            if index == len(brackets) - 1:
                # 比brackets最后一个还大
                if income - brackets[index][0] < 0:
                    tax += (income - brackets[index - 1][0]) * brackets[index][1] / 100
                    return tax
            if income >= brackets[index][0]:
                tax += (brackets[index][0]- brackets[index-1][0]) * brackets[index][1] / 100
            if income < brackets[index-1][0]:
                break
            index += 1
        return tax

print(Solution.calculateTax(Solution(), brackets = [[1,0],[4,25],[5,50]], income = 2))