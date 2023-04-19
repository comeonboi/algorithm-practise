from typing import List


class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        str1 = ""
        board = ["abcde",
                 "fghij",
                 "klmno",
                 "pqrst",
                 "uvwxy",
                 "z"]
        now_i = 0
        now_j = 0
        for i in board:
            for j,value in enumerate(i):
                pass
        for char in target:
            # 查看在哪一行
            for i in range(len(board)):
                if char in board[i]:
                    if i - now_i > 0:
                        str1 += 'D' * (i - now_i)
                    if i - now_i < 0:
                        str1 += 'U' * (now_i - i)
                    now_i = i
                    # 在哪一列
                    for j, value in enumerate(board[i]):
                        if value == char:
                            if j - now_j > 0:
                                str1 += 'R' * (j - now_j)
                            if j - now_j < 0:
                                str1 += 'L' * (now_j - j)
                            str1 += '!'
                            now_j = j
        return str1


class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        i = j = 0
        ans = []
        for char in target:
            v = ord(char) - ord("a")
            x, y = v // 5, v % 5
            while j > y:
                j -= 1
                ans.append("L")
            while i > x:
                i -= 1
                ans.append("U")
            while j < y:
                j += 1
                ans.append("R")
            while i < x:
                i += 1
                ans.append("D")
            ans.append("!")
        return "".join(ans)


print(Solution.alphabetBoardPath(Solution(), target="code"))
