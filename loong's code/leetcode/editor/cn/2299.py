import re


class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        flag1 = flag2 = flag3 = flag4 = 1

        ret = None
        for i in password:
            if ret == i:
                return False
            if i.isdigit():
                flag1 = 0
            elif i.isupper():
                flag2 = 0
            elif i.islower():
                flag3 = 0
            else:
                flag4 = 0
            ret = i
        if sum([flag1, flag2, flag3, flag4]) == 0 and len(password) >= 8:
            return True
        return False


print(Solution.strongPasswordCheckerII(Solution(), password="IloveLe3tcode!"))
