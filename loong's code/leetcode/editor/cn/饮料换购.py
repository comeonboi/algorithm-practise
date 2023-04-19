from typing import List
import os
import sys

# 请在此输入您的代码
n = int(input())
ans = n
while n != 0:
    m = n % 3
    n //= 3
    ans += n
    if n == 0:
        break
    n = n + m
print(ans)
