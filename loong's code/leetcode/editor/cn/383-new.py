import collections


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        # for i in ransomNote:
        #     if i not in magazine:
        #         return False
        #     else:
        #         magazine = magazine.replace(i, '_', 1)
        # return True
        return not collections.Counter(ransomNote)-collections.Counter(magazine)

print(Solution.canConstruct(Solution, ransomNote="aa", magazine="ab"))
