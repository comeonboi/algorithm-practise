from typing import List
import re
file = input()
pattern = r'([^=;\s]+)|([^=;\s]+)=([^;]+);?'
first = re.search(pattern, file)
f_k = first.group(1)
file = file.replace(first.group(), '', 1)
result = re.findall(pattern, file)
d = {f_k: result[0][1]}
for key, value in result[1:]:
    d[key] = value
q = int(input())
for _ in range(q):
    son = input()
    # index = file.rfind(son)
    # # print(index, index + len(son) + 1)
    # if index != -1:
    #     index2 = file.find(';', index)
    #     # # while file[index] == ';':
    #     # #     str1 += ''
    #     # print(index2)
    #     print(file[index + len(son) + 1:index2])
    # else:
    #     print('EMPTY')
    if son in d:
        print(d[son])
    else:
        print('EMPTY')
