class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n=1
        while (n<len(s)):
            if len(s)%len(s[:n]) == 0:
                times = len(s)//len(s[:n])
                if s[:n]*times==s:
                    return True
                else:
                    n+=1
            else:
                n+=1
        return False
