import matplotlib.pyplot as plt
import numpy as np

# step1：生成一个网点图
length, width = 50, 50  # 定义迷宫大小
maze = np.zeros(shape=(length, width))
maze[::2, ::2] = 1

# 每次只能上下左右试探
step_set = np.array([[1, 0],
                     [-1, 0],
                     [0, 1],
                     [0, -1]])


def find_next_step(maze, point, step_set):
    # 用递归实现深度优先搜索
    step_set = np.random.permutation(step_set)
    for next_step in step_set:
        next_point = point + next_step * 2
        x, y = next_point
        if 0 <= x < length and 0 <= y < width:  # 在格子内
            if maze[x, y] == 1:  # 如果还没打通，就打通
                maze[x, y] = 2
                maze[(point + next_step)[0], (point + next_step)[1]] = 2
                maze, _, _ = find_next_step(maze, next_point, step_set)  # 深度优先搜索
    # 全部遍历后，还是找不到，就是这个叶节点没有下一步了，返回即可
    return maze, point, step_set


# 定义起点
point = np.array([0, 0])
find_next_step(maze, point, step_set)

# 至于终点，道路上的每个点都可以作为终点
plt.imshow(maze)
plt.show()
