#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def binary_search(lst, target):
    left, right = 0, len(lst) - 1  # 初始化查找区间的左右边界
    while left <= right:  # 当左右边界没有重叠时，循环执行二分查找
        mid = (left + right) // 2  # 计算中间位置
        if lst[mid] == target:  # 如果中间位置的元素等于目标元素，返回该元素
            return lst[mid]
        elif lst[mid] < target:  # 如果中间位置的元素小于目标元素，将查找区间缩小到右半部分
            left = mid + 1
        else:  # 如果中间位置的元素大于目标元素，将查找区间缩小到左半部分
            right = mid - 1

    # 如果查找完毕后没有找到目标元素，我们需要返回离目标元素最近的参考值
    if left > len(lst) - 1:  # 如果左边界越界，说明目标元素比所有元素都大，返回最大元素
        return lst[-1]
    elif right < 0:  # 如果右边界越界，说明目标元素比所有元素都小，返回最小元素
        return lst[0]
    else:  # 如果左右边界都在列表范围内，比较左右边界对应的元素，返回最接近目标元素的那个元素
        if abs(lst[left] - target) < abs(lst[right] - target):
            return lst[left]
        else:
            return lst[right]
def gradingStudents(grades):
    grade = list(range(0,101,5))
    ans = []
    for i in grades:
        if i > 33:
            if i % 5 >= 3:
                ans.append(binary_search(grade, i))
            else:
                ans.append(i)
        else:
            ans.append(i)

    return ans

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)
    print(result)
    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')
    #
    # fptr.close()
