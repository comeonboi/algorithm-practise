from collections import defaultdict
#
# n = int(input())
# qi_pan = []
# queen_site = defaultdict(list)
# ans = 0
# for i in range(n):
#     lie = list(input().strip())
#     # 记录皇后的位置
#     if "*" in lie:
#         for j,x in enumerate(lie):
#             if x == '*':
#                 queen_site[str(i)].append(j)
#     qi_pan.append(lie)
# # 如果本行没有皇后
# for flag, hang in enumerate(qi_pan):
#     if "*" not in hang:
#         for i,x in enumerate(hang):
#             current_site = (flag, i)
#             variable = 0
#             if flag > 0:
#                 for qs in queen_site[str(flag - 1)]:
#                     # 只判断上下一行
#                     if i == qs + 1 or\
#                         i == qs - 1 or \
#                             i == qs:
#                         break
#                 else:
#                     for qs in queen_site:
#                         if i in queen_site[qs]:
#                             break
#                     else:
#                         variable += 1
#             if flag < n and variable == 1:
#                 for qs in queen_site[str(flag + 1)]:
#                     # 只判断上下一行
#                     if i == qs + 1 or\
#                         i == qs - 1 or \
#                             i == qs:
#                         break
#                 else:
#                     for qs in queen_site:
#                         if i in queen_site[qs]:
#                             break
#                     else:
#                         variable += 1
#             if variable == 2:
#                 ans += 1
#
# print(ans)

n = int(input())
count_hang = defaultdict(int)
count_lie = defaultdict(int)
count_diagonal = defaultdict(int)
count_con_diagonal = defaultdict(int)
chessboard = []
ans = 0


for i in range(n):
    hang = list(input().strip())
    chessboard.append(hang)
    # record where the queen is
    if "*" in hang:
        for index_j, j in enumerate(hang):
            if j == "*":
                count_hang[str(i)] += 1
                count_lie[str(index_j)] += 1
                count_diagonal[str(i+index_j)] += 1
                count_con_diagonal[str(i-index_j)] += 1
for index_i, i in enumerate(chessboard):
    if "*" not in i:
        for index_j, j in enumerate(i):
            if count_lie[str(index_j)] == \
                    count_hang[str(index_i)] \
                    == count_diagonal[str(index_i+index_j)] ==\
                    count_con_diagonal[str(index_i-index_j)] == 0:
                ans += 1
print(ans)