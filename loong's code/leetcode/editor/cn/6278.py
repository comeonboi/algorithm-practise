class Solution:
    def countDigits(self, num: int) -> int:
        flag = 0
        list1 = ''.join(str(num))
        for i in list1:
            if num % int(i) == 0:
                flag += 1
        return flag


print(Solution.countDigits(Solution(), num=1248
                           ))
