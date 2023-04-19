from typing import List


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        if len(skill) % 2 != 0:
            return -1
        skill = sorted(skill)
        tail = len(skill) - 1
        sum1 = skill[0] + skill[-1]
        cheng = 0
        for i in range(0, len(skill) // 2):
            if sum1 != skill[i] + skill[tail - i]:
                return -1
            else:
                cheng += skill[i] * skill[tail - i]
        return cheng


print(Solution.dividePlayers(Solution(), skill=[1,1,2,3]))
