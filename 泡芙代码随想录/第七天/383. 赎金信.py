class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote_dict = {}
        magazine_dict = {}
        for i in range(len(ransomNote)):
            if ransomNote[i] not in ransomNote_dict:
                ransomNote_dict[ransomNote[i]] = 1
            else:
                ransomNote_dict[ransomNote[i]] += 1
        for i in range(len(magazine)):
            if magazine[i] not in magazine_dict:
                magazine_dict[magazine[i]] = 1
            else:
                magazine_dict[magazine[i]] += 1
        for key in ransomNote_dict.keys():
            if key not in magazine_dict:
                return False
            else:
                if ransomNote_dict[key] > magazine_dict[key]:
                    return False
        return True