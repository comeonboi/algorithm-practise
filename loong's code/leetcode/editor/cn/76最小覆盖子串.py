from typing import List
from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans = 1000001
        hash_1 = {}

        def isAll(dict_keys, target):
            for i in target:
                if i not in dict_keys:
                    return False
                else:
                    if dict_keys[i] < target[i]:
                        return False
            return True

        dict_t = Counter(t)
        left = 0
        right = 0
        while right < len(s):
            # 当不存在t里所有元素的时候，右指针右移
            # 当存在t里所有元素的时候，左指针右移，如果右指针没有到最右边，继续移动右指针
            # 如果找到t，跳出返回
            dict1 = Counter(s[left:right + 1])
            # 如果有所有元素了
            if isAll(dict1, dict_t):
                ans = min(ans, right - left + 1)
                hash_1[right - left + 1] = s[left:right+1]
                print(ans, hash_1)
                left += 1
            else:
                right += 1
            print(ans, hash_1, dict1.keys())
        return hash_1[ans] if len(hash_1) != 0 else ""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 存储t字符串中每个字符的数量
        dict_t = Counter(t)
        # 存储当前滑动窗口中的字符
        dict_keys = {}
        # 左指针和右指针
        left = 0
        right = 0
        # 记录最小长度
        min_len = float('inf')
        # 记录最短字符串的起始位置和结束位置
        start = 0
        end = 0
        # 右指针从0到len(s) - 1依次滑动
        while right < len(s):
            # 如果当前字符在t中，则把它加入当前滑动窗口的字典中
            if s[right] in dict_t:
                dict_keys[s[right]] = dict_keys.get(s[right], 0) + 1
            # 如果当前滑动窗口中包含了t中的所有字符
            while right < len(s) and isAll(dict_keys, dict_t):
                # 如果当前长度小于之前记录的最小长度，更新最小长度和起始位置和结束位置
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start = left
                    end = right
                # 左指针右移，把当前字符从当前滑动窗口的字典中移除
                if s[left] in dict_keys:
                    dict_keys[s[left]] -= 1
                    if dict_keys[s[left]] == 0:
                        del dict_keys[s[left]]
                left += 1
            right += 1
        # 返回最短字符串，如果没有则返回空字符串
        return s[start:end + 1] if min_len != float('inf') else ""

def isAll(dict_keys, target):
    for key in target:
        if key not in dict_keys or dict_keys[key] < target[key]:
            return False
    return True

print(Solution.minWindow(Solution(), s = "cabwefgewcwaefgcf", t = "cae"))
