from typing import List
import os
import sys

prime = ['2', '3', '5', '7']


# prime
def is_prime(n: str):
    for i in n:
        if i not in prime:
            return False
    n = int(n)
    for i in range(2, int(n ** 0.5)):
        if n % i == 0:
            return False
    return True


def child(num):
    ans = []
    for i in range(0, len(num)-1):
        for j in range(i + 1, len(num)):
            ans.append(num[i:j + 1])
    for ch in ans:
        div = is_prime(ch)
        if not div:
            return False
    return True


for nums in range(9999, 2, -1):
    if child(str(nums)) and is_prime(str(nums)) :
        print(nums)
        break
