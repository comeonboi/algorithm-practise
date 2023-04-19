from typing import List

a, b, n = map(int, input().split(" "))
# print(a, b, n)
q = n // (5*a+2*b) * 7
# 余下的题目
r = n % (5*a+2*b)
if r > 5 * a:
    if r - 5 * a < b:
        q += 6
    else:
        q += 7
    print(q)
elif r == 0:
    print(q)
else:
    if r % a != 0:
        q += (r // a) + 1
    else:
        q += (r // a)
    print(q)
