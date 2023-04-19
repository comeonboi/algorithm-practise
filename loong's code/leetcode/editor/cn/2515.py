from typing import List


class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        min_flag = 9999999
        def findMin(min_flag, single):
            flag = 0
            i = startIndex
            while 1:
                i = i % len(words)
                if words[i] == target:
                    min_flag = min(flag, min_flag)
                    break
                flag += 1
                if single == '+':
                    i += 1
                else:
                    i -= 1
            return min_flag
        min_flag = findMin(min_flag, '+')
        min_flag = findMin(min_flag, '-')
        return min_flag


print(Solution.closetTarget(Solution(),words = ["hsdqinnoha","mqhskgeqzr","zemkwvqrww","zemkwvqrww","daljcrktje",
                                                "fghofclnwp","djwdworyka","cxfpybanhd","fghofclnwp","fghofclnwp"]
                            , target = "zemkwvqrww", startIndex = 8))