from collections import Counter, defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        list1 = {}
        list2 = []
        flag = 0
        for i in strs:
            x = dict(Counter(i))
            if x not in list2:
                list1[flag] = [i]
                list2.append(x)
                flag += 1
            elif x in list2:
                flag2 = 0
                for j in list2:
                    if j == x and i not in list1:
                        list1[flag2].append(i)
                    flag2 += 1
        return list(list1.values())

print(Solution.groupAnagrams(Solution(), strs = ["eat", "tea", "tan", "ate", "nat", "bat"]))


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        思路：1.字母异位词指字符串中包含的字母相同
             2.找到相同点作为哈希表的key——key:排序后的字符串 value:字母异位词列表
        方法：哈希表
        """

        map_data = defaultdict(list)
        for str in strs:
            key = "".join(sorted(str))
            map_data[key].append(str)
        return list(map_data.values())
print(Solution.groupAnagrams(Solution(), strs = ["eat", "tea", "tan", "ate", "nat", "bat"]))
