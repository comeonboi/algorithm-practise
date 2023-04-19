from typing import List


class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        ans = []
        record = {}
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if k not in record:
                        if (i,j) not in record.values():
                            record[k] = (i,j)
                            flag = (nums[i]|nums[j])&nums[k]
                            if flag not in ans:
                                ans.append(flag)
                            else:
                                ans.remove(flag)
        if len(ans) == 0:
            return 0
        answer = ans[0]

        for i in range(1,len(ans)):
            answer ^= ans[i]
        return answer

print(Solution.xorBeauty(Solution,nums = [38,42,42,13,18,30,3,41,40,15]))