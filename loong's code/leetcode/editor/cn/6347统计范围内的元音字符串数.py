from typing import List


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        # 创建一个元音集合
        yuanyin = set('aeiou')
        # 遍历每个单词，判断它的首尾字母是否都是元音
        # 将结果存入 words_first_last 列表中
        words_first_last = [(word[0] in yuanyin and word[-1] in yuanyin) for word in words]

        # 创建一个 counts 列表，用来存储前缀和
        counts = [0] * (len(words) + 1)
        # 遍历每个单词，计算前缀和
        for i in range(len(words)):
            counts[i + 1] = counts[i] + int(words_first_last[i])
        # 遍历每个查询，计算该查询的结果
        ans = []
        for i, j in queries:
            ans.append(counts[j+1] - counts[i])
        # 返回结果
        return ans


print(Solution.vowelStrings(Solution(), words=["aba", "bcb", "ece", "aa", "e"], queries=[[0, 2], [1, 4], [1, 1]]))
