class Solution:
    def smallestValue(self, n: int) -> int:
        if iszhishu(n) == 1 or n == 4:
            return n
        else:
            while iszhishu(n) != 1:
                list1 = fenjie(n)
                n = sum(list1)
            return n


def iszhishu(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
        else:
            return True


def fenjie(n):
    list1 = []
    num = n
    while n != 1:
        i = 2
        while i <= n:
            if n % i == 0:
                list1.append(i)
                n //= i
            else:
                i += 1
        if n == 1:
            break
    return list1


print(Solution.smallestValue(Solution, n=27))
