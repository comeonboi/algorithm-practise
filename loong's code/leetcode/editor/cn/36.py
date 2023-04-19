import numpy as np


def isValidSudoku(board: list[list[str]]) -> bool:
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == '.':
                board[i][j] = '-1'
    sada = np.array(board)
    for i in sada:
        List = []
        for j in i:
            if j in List:
                return False
            if int(j) > 0:
                List.append(j)

    for i in range(sada.shape[1]):
        print(sada[:, i])
        List = []
        for j in sada[:, i]:
            if j in List:
                return False
            if int(j) > 0:
                List.append(j)
    for i in range(0, 9, 3):  # 对九宫格是否重复进行判断
        for j in range(0, 9, 3):
            storage = []
            for x in range(0, 3):
                for y in range(0, 3):
                    if sada[i + x][j + y] == '-1':
                        continue
                    if sada[i + x][j + y] in storage:
                        return False
                    else:
                        storage.append(sada[i + x][j + y])
    return True


print(isValidSudoku(board=
                    [[".", ".", ".", ".", "5", ".", ".", "1", "."], [".", "4", ".", "3", ".", ".", ".", ".", "."],
                     [".", ".", ".", ".", ".", "3", ".", ".", "1"], ["8", ".", ".", ".", ".", ".", ".", "2", "."],
                     [".", ".", "2", ".", "7", ".", ".", ".", "."], [".", "1", "5", ".", ".", ".", ".", ".", "."],
                     [".", ".", ".", ".", ".", "2", ".", ".", "."], [".", "2", ".", "9", ".", ".", ".", ".", "."],
                     [".", ".", "4", ".", ".", ".", ".", ".", "."]]))
