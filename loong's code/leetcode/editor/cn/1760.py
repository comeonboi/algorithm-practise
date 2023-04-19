class Solution:
    def minimumSize(self, nums: list[int], maxOperations: int) -> int:
        # 【参考提示】【重点：理解题意，将题目转化为可以实现的问题】如果一个袋子最多只能装x个，需要拆分y次；每个袋子能能装的球数越多，则需要拆分的次数越少（具有单调性）
        # 当y>maxOperations时，说明x不合题意，则x+=1，第一次当y=maxOperations时的x即为符合题意的答案（此过程可以用二分查找）

        def oper_time(x):
            # x是每个袋子最多装的球个数，返回拆分次数
            oper = 0
            for bag in nums:
                if bag > x:
                    oper += (bag - 1) // x
            return oper

        # 进行二分查找 因为oper_time是随着x的增加单调递减的
        l, r = 1, max(nums)
        if oper_time(l) == maxOperations:
            return l
        while l < r:
            mid = (l + r) // 2
            if oper_time(mid) <= maxOperations:
                r = mid
            else:
                l = mid + 1
        return l


print(Solution.minimumSize(Solution(), nums=[9], maxOperations=2))