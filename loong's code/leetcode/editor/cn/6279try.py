import math
from functools import reduce
import random
from typing import List

import ll
from jedi.api.refactoring import inline


class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        result1 = reduce((lambda x, y: x * y), nums)
        f = Rho_Heuristic(result1)
        print(f)
        return len(set(f))


random.seed(0)


def Rho_Heuristic(n):
    cum_d = 1
    x = random.randint(0, n - 1)
    y = x
    k = 2
    i = 1
    while not (cum_d == n):
        i = i + 1
        x = (x * x - 1) % n
        d = math.gcd(y - x, n)
        if not (d == 1) and not (d == n):
            print(d)
            cum_d = (d * cum_d)
        if i == k:
            y = x
            k = 2 * k


print(Solution.distinctPrimeFactors(Solution(),
                                    nums=[2, 4, 3, 7, 10, 6]))
