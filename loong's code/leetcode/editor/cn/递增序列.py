from typing import List

matrix = []
s = input().replace("\n", "")
n, m = 30, 50
sub_strs = [list(s[i:i + m]) for i in range(0, len(s), m)]
ans = 0
# lst = [[sub_strs[i][j:j+n] for j in range(0, m, n)] for i in range(len(sub_strs))]
for i in range(len(sub_strs)):
    for j in range(len(sub_strs[i])):
        # 横
        k = 0
        while j + k < m:
            if sub_strs[i][j] < sub_strs[i][j + k]:
                ans += 1
                # aa.append(sub_strs[i][j]+sub_strs[i][j+k])
            k += 1
        # 竖
        k = 0
        while i + k < n:
            if sub_strs[i][j] < sub_strs[i + k][j]:
                ans += 1
                # aa.append(sub_strs[i][j]+sub_strs[i+k][j])
            k += 1
        # 右下
        k = 0
        while i + k < n and j + k < m:
            if sub_strs[i][j] < sub_strs[i + k][j + k]:
                ans += 1
                # aa.append(sub_strs[i][j]+sub_strs[i+k][j+k])
            k += 1
        # 左下
        k = 0
        while i + k < n and j - k >= 0:
            if sub_strs[i][j] < sub_strs[i + k][j - k]:
                ans += 1
                # aa.append(sub_strs[i][j]+sub_strs[i+k][j-k])
            k += 1
        # 右上
        k = 0
        while i - k >= 0 and j + k < m:
            if sub_strs[i][j] < sub_strs[i - k][j + k]:
                ans += 1
                # aa.append(sub_strs[i][j]+sub_strs[i-k][j+k])
            k += 1
print(ans)
