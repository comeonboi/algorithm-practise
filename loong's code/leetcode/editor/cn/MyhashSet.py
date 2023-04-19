from collections import defaultdict, Counter
from typing import List


class Solution:

    def containsDuplicate(self, nums: List[int]) -> bool:
        dict1 = Counter(nums)
        dict1 = sorted(dict1.values())
        if dict1[-1] >= 2:
            return True
        else:
            return False

    def singleNumber(self, nums: List[int]) -> int:
        dict1 = Counter(nums)
        a = sorted(dict1.items(), key=lambda x: x[1], reverse=False)
        return a[0][0]

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        return list(nums1 & nums2)

    def isHappy(self, n: int) -> bool:
        list1 = []
        ans = n
        while 1:
            ans = list(map(int, list(str(ans))))
            ans = sum(map(lambda x: x ** 2, ans))
            if ans == 1:
                return True
            if ans not in list1:
                list1.append(ans)
            else:
                return False

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        start = 0
        tail = len(nums) - 1
        nnn = nums
        nums = sorted(nums)
        while 1:
            sums = nums[start] + nums[tail]
            if sums == target:
                break
            if sums < target:
                start += 1
            else:
                tail -= 1
            # if start == target:
            #     return []
        qwe = []
        flag = 0
        for i in nnn:
            if i == nums[start]:
                if flag not in qwe:
                    qwe.append(flag)
            if i == nums[tail]:
                if flag not in qwe:
                    qwe.append(flag)
            flag += 1
        return qwe

print(Solution.twoSum(Solution(), nums=[3,3], target=6))


class MyHashSet:

    def __init__(self):
        self.hash_list = []

    def add(self, key: int) -> None:
        if key in self.hash_list:
            pass
        else:
            self.hash_list.append(key)

    def remove(self, key: int) -> None:
        if key in self.hash_list:
            self.hash_list.remove(key)

    def contains(self, key: int) -> bool:
        if key in self.hash_list:
            return True
        else:
            return False


class MyHashMap:

    def __init__(self):
        self.hash_dict = defaultdict()

    def put(self, key: int, value: int) -> None:
        if key not in self.hash_dict:
            self.hash_dict[key] = value
        else:
            self.hash_dict[key] = value

    def get(self, key: int) -> int:
        if key in self.hash_dict:
            return self.hash_dict[key]
        else:
            return -1

    def remove(self, key: int) -> None:
        if key in self.hash_dict:
            del self.hash_dict[key]
