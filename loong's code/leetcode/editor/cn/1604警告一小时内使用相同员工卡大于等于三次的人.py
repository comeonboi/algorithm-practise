from collections import defaultdict
from typing import List


class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        ans = set()
        dict1 = defaultdict(list)
        for name, time in zip(keyName, keyTime):
            dict1[name].append(int(time[:2])*60+int(time[3:]))
        print(dict1)
        for i in dict1:
            # 定义10：00-11：00出现三次计数，就警告
            if len(dict1[i]) >= 3:
                dict1[i].sort()
                print(dict1[i])
                for j in range(len(dict1[i])):
                    # 遍历当前小时到一小时内,好像可以直接看切片
                    # for k in range(len(dict1[i]) + 1, len(dict1[i])+3):
                    if j + 2 < len(dict1[i]):
                        # if dict1[i][j:j + 3][0].replace(":", "")[:2]
                        if abs(dict1[i][j:j + 3][-1] -
                            dict1[i][j:j + 3][0]) <= 60:
                            ans.add(i)
                        print(dict1[i][j:j + 3])
        ans = list(ans)
        ans.sort()
        return ans


print(Solution.alertNames(Solution(), keyName = ["a","a","a","a","a","b","b","b","b","b","b"]
                          , keyTime = ["04:48","23:53","06:36","07:45","12:16","00:52","10:59","17:16","00:36","01:26","22:42"]))
