class Solution:
    def isHappy(self, n: int) -> bool:
        n = str(n)
        exist_dict = {}
        square_sum = 0
        while n not in exist_dict:
            for i in range(len(n)):
                square_sum += int(n[i]) ** 2
            if square_sum == 1:
                break
            else:
                exist_dict[n] = 1
                n = str(square_sum)
                square_sum = 0
        if square_sum == 1:
            return True
        else:
            return False
