class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        # 三个数一样的三元组是1个
        # 1 + 2的三元组是3个
        res = 0
        n = len(nums)
        for i in range(32):
            cnt = [0, 0]
            for num in nums:
                cnt[(num >> i) & 1] += 1
            tmp = 0
            for num in nums:
                cur = (num >> i) & 1
                if cur == 1:
                    tmp ^= (n * cnt[1] % 2)
                else:
                    tmp ^= (cnt[1] * cnt[1] % 2)
            res += (tmp << i)
        return res