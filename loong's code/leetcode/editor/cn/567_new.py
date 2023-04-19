import collections


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 窗口大小为s1的长度，我们使用一个长度和 s1长度相等的固定窗口大小的滑动窗口
        # 在 s2上面从左向右滑动，判断 s2在滑动窗口内的每个字符出现的个数是否跟 s1每个字符出现次数完全相等。
        # dicts = {}
        # for i in s1:
        #     if i not in dicts:
        #         dicts[i] = 1
        #     else:
        #         dicts[i] += 1
        window = len(s1)
        dicts = collections.Counter(s1)
        if not dicts:
            return True
        # 运行时间很高
        # for i in range(len(s2)):
        #     dist2 = collections.Counter(s2[i:i + window])
        #     if dist2 == dicts:
        #         return True
        # return False
        left = 0
        right = len(s1) - 1
        dicts2 = collections.Counter(s2)
        counter2 = collections.Counter(s2[0:right])
        print(dicts2, counter2)
        while right < len(s2):
            # 窗口右移，右边的元素+1
            counter2[s2[right]] += 1
            if dicts == counter2:
                return True
            # 窗口左移，左边的-1
            counter2[s2[left]] -= 1
            # 如果为0，就删除这个
            if counter2[s2[left]] == 0:
                del counter2[s2[left]]
            left += 1
            right += 1
print(Solution.checkInclusion(Solution, s1="abo", s2="eidbaooo"))
