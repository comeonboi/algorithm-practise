class Solution:
    def isPalindrome(self, s: str) -> bool:
        for i in s:
            if i.isalpha() != 1 and i.isalnum() != 1:
                s = s.replace(i, '')
            if i.isupper():
                s = s.lower()
        if s[::-1] == s:
            return True
        else:
            return False


print(Solution.isPalindrome(Solution, s="0P"))
