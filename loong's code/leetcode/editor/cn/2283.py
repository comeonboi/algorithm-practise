from collections import Counter


class Solution:
    def digitCount(self, num: str) -> bool:
        hash_1 = {}
        for index, i in enumerate(num):
            if int(i) != 0:
                hash_1[str(index)] = int(i)
        hash_2 = Counter(num)
        if hash_1 == dict(hash_2):
            return True
        return False

print(Solution.digitCount(Solution,num = "1210"))