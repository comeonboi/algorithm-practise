from collections import defaultdict
from typing import List


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        """
        思路：将所有字符串转化成一种模式——以a****开头
        方法：哈希表
        """
        mp_data = defaultdict(list)
        for str in strings:
            if str[0] == 'a':
                mp_data[str].append(str)
            else:
                tmp = list(str)
                for i in range(len(str)):
                    tmp[i] = chr((ord(tmp[i]) - ord(str[0]) + 26) % 26 + ord('a'))
                tmp = ''.join(tmp)
                mp_data[tmp].append(str)
        return list(mp_data.values())

