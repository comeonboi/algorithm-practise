from typing import List
import collections
def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
    ans = num = 0
    cnt = collections.Counter()
    for i, j in sorted(zip(values, labels), reverse=True):
        if cnt[j] < useLimit:
            cnt[j] += 1
            num += 1
            ans += i
            if num == numWanted:
                break
    return ans