from typing import List
import os
import sys

from decimal import Decimal

# 请在此输入您的代码
n = int(input())
grade = [int(input()) for i in range(n)]


# 平均分保留两位小数
def mean():
    return sum(grade) / n


print(max(grade), '\n', min(grade), '\n', Decimal("%.2f" % mean()), sep='', end='')
