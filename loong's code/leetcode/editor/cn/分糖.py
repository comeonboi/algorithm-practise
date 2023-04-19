from functools import cache
from typing import List


@cache
def calculate_tail():
    max_sums = 0
    for i in range(m):
        sums = 0
        for tail in range(m):
            if head + tail * 3 + i <= n - 1:
                index = head + tail * 3 + i
                tails.append(index)
                sums += x_list[index]
        max_sums = max(max_sums, sums)
    return max_sums


n = int(input())
x_list = list(map(int, input().split()))
max_del = 0
# 最多可以选择的糖果数量
m = (n + 2) // 3
for head in range(n):
    # 尾指针数组
    tails = []
    max_del = max(max_del, calculate_tail())

print(max_del)
