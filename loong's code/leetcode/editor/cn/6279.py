from functools import reduce
from typing import List


class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        result1 = reduce((lambda x, y: x * y), nums)
        f = nxyz(result1)
        return len(set(f))


def nxyz(fi):  # 整数的因式分解公式，
    xd = list()  # 因子存于此处
    if fi <= 3:
        xd.append(fi)
    if fi >= 4:
        x = 2
        while fi >= x ** 2:
            if fi % x != 0:
                x += 1
            if fi % x == 0:
                xd.append(str(x))
                fi = int(fi // x)
        xd.append(str(fi))
    if len(xd) == 1 and fi != 1:
        return xd
    if fi == 1:
        pass
    if len(xd) > 1:
        return xd

print(Solution.distinctPrimeFactors(Solution(),nums=[]))

class Solution:
    def distinctPrimeFactors(self,nums: List[int]) -> int:
        nums = set(nums)
        product,divisor = 1,2
        prime = set()
        for num in nums:
            product *= num
        while product != 1:
            if product % divisor == 0:
                product //= divisor
                prime.add(divisor)
            else:
                divisor += 1
        return len(prime)