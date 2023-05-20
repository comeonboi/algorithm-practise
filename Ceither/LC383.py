import collections
def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    cmag = Counter(magazine)
    for i in ransomNote:
        if cmag.get(i):
            cmag[i] -= 1
        else:
            return False
    return True