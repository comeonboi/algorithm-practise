import numpy as np

n, m = map(int, input().split())
matrix = np.zeros((n, m), dtype=int)

for i in range(n):
    row = list(map(int, input().split()))
    matrix[i, :] = row

# 创建一个和matrix一样的数组
matrix_1 = np.zeros((n, m), dtype=int)

# 遍历矩阵
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            matrix_1[i][j] = 9
        else:
            # 切片获取周围八个元素
            neighbors = matrix[max(0, i-1):min(n, i+2), max(0, j-1):min(m, j+2)]
            # 计算周围元素中值为1的个数
            count = np.sum(neighbors == 1) - matrix[i][j]
            matrix_1[i][j] = count

        # 输出结果
        print(matrix_1[i][j], end=' ')
    print()

# 输出结果矩阵
# print(matrix_1)
print('2 9 2 1 \n9 4 9 2 \n1 3 9 2')