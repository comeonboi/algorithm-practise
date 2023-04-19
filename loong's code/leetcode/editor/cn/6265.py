import collections


class Solution:
    def similarPairs(self, words: list[str]) -> int:
        flag = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if collections.Counter(words[i]).keys() == collections.Counter(words[j]).keys():
                    flag += 1
        return flag


print(Solution.similarPairs(Solution, words = ["aabb","ab","ba"]))
