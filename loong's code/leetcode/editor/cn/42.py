import numpy as np


class Solution:
    def trap(self, height: list[int]) -> int:
        chang = len(height)
        kuan = max(height)
        x = np.zeros([chang, kuan], dtype=int)
        flag = 0
        for i in height:
            x[flag][kuan - i:] = 1
            flag += 1
        x = np.flip(x, axis=1)
        x = np.rot90(x, 1)
        x = np.flip(x, axis=0)
        i = 0
        print(x)
        flag = 0
        while i < kuan:
            j = 0
            while j < chang:
                # 找对应的列有多高，直接跳到对应的点
                if x[i][j] == 1:
                    # 从这点开始往右看, True
                    # if x[height[j] - 1][j] == 1:
                    # 双指针
                    qw = recursion(x, i, j, chang, kuan, height)
                    # x[i][j + 1:j + qw + 1] = 2
                    flag += qw
                j += 1
            i += 1
        # flag = 0
        #
        # for i in range(kuan):
        #     for j in range(chang):
        #         if x[i][j] == 2:
        #             flag += 1
        # flag = np.sum(x == 2)
        return flag


def recursion(x, i, j, chang, kuan, height) -> int:
    flag = 0
    while 0 <= i < kuan and 0 <= j < chang:
        if chang > j + 1 >= 0:
            if x[i][j + 1] == 0:
                j = j + 1
                flag += 1
            else:
                return flag
        else:
            return 0


print(Solution.trap(Solution(), height=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
