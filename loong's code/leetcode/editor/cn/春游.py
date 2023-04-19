from typing import List


def square(x):
    return pow(x, 2)


n, m = map(int, input().split())
a = sorted(list(map(square, map(float, input().split()))))
# print(a)
q = list(map(int, input().split()))
ans = []
for i in q:
    for j in range(n - 1, -1, -1):
        # print(a[:j+1])
        if sum(a[:j + 1]) <= i:
            # print("j", a[:j+1])
            ans.append(j + 1)
            break
    else:
        ans.append(0)

for ind, i in enumerate(ans):
    if ind != len(ans) - 1:
        print(i, end=" ")
    else:
        print(i, end="")
