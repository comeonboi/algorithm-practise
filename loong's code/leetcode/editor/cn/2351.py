class Solution:
    def repeatedCharacter(self, s: str) -> str:
        dict1 = {}
        for i in s:
            if i not in dict1:
                dict1[i] = 1
            else:
                dict1[i] += 1
            if dict1[i] == 2:
                return i


print(Solution.repeatedCharacter(Solution(), s="abccbaacz"))
