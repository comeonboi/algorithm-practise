# import itertools
#
# nums = set()
# for i in range(2, 1000):
#     for j in range(2, 100):
#         if i not in nums:
#             sums = i ** j
#             if sums > 10**18:
#                 break
#             nums.add(sums)
# nums2 = set(map(lambda x: x[0] * x[1], itertools.product(nums, repeat=2)))
# nums.union(nums2)
# result = set()
#
# while True:
#     try:
#         a = int(''.join(list(map(str, input().strip().split()))))
#         flag = 0
#         if a in nums:
#             print('yes')
#         else:
#             for i in range(1, a + 1):
#                 if a % i == 0:
#                     if i in nums and a // i in nums:
#                         flag = 1
#                         print(a, 'yes', i, a // i)
#                         break
#             if flag != 1:
#                 print(a, 'no')
#     except():
#         break
# import math
# #这个程序确实可以正确地解决问题，但它的时间复杂度是O(T*sqrt(ai))，对于评测用例中的最大数字 10^18，运行时间将会很长。
#
# #为了更快的运行时间，可以使用线性筛法来预处理质数，并使用质数筛法来筛选质因子。这样的时间复杂度将会是O(T*log(log(ai))),这样就能满足在1s内运行的需求了。
#
# import itertools
# #
# # def primeFactorization(n, primes):
# #     factors = {}
# #     for i in range(2, int(n ** 0.5) + 1):
# #         if primes[i]:
# #             while n % i == 0:
# #                 if i not in factors:
# #                     factors[i] = 1
# #                 else:
# #                     factors[i] += 1
# #                 n = n // i
# #     if n > 1:
# #         factors[n] = 1
# #     return factors
# #
# # def SieveOfEratosthenes(n):
# #     prime = [True for i in range(n + 1)]
# #     p = 2
# #     while (p * p <= n):
# #         if (prime[p] == True):
# #             for i in range(p * 2, n + 1, p):
# #                 prime[i] = False
# #         p += 1
# #     return prime
# #
# # primes = SieveOfEratosthenes(int(10 ** 6))
# # nums = set()
# # for i in range(2, int(10 ** 6)):
# #     if primes[i]:
# #         for j in range(2, 30):
# #             temp = i ** j
# #             if temp > 10 ** 18:
# #                 break
# #             nums.add(temp)
# #
# # while True:
# #     try:
# #         a = int(input())
# #         factors = primeFactorization(a, primes)
# #         if len(factors) == 1 and max(factors.values()) >= 2:
# #             print("yes")
# #         else:
# #             print("no")
# #     except:
# #         break
def primeFactorization(n, primes):
    factors = {}
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            while n % i == 0:
                if i not in factors:
                    factors[i] = 1
                else:
                    factors[i] += 1
                n = n // i
    if n > 1:
        factors[n] = 1
    return factors


def SieveOfEratosthenes(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    return prime


primes = SieveOfEratosthenes(int(10 ** 6))
nums = {}
for i in range(2, int(10 ** 6)):
    if primes[i]:
        for j in range(2, 30):
            temp = i ** j
            if temp > 10 ** 18:
                break
            if temp not in nums:
                nums[temp] = 1

while True:
    try:
        a = int(input())
        factors = primeFactorization(a, primes)
        if len(factors) == 1 and max(factors.values()) >= 2:
            print("yes")
        else:
            if a in nums:
                print("yes", a)
            else:
                print("no", a)
    except:
        break
