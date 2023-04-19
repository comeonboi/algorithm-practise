class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        diff = maxSum - n
        left = index
        right = index
        res = 1
        dl = 0
        dr = 0
        while diff > 0:  # 当还有剩余砖块时
            left -= 1
            right += 1
            if left >= 0:
                dl = dl + 1  # 尚未到达左边界
            if right < n:
                dr = dr + 1  # 尚未到达右边界
            if left < 0 and right >= n:  # 当到达左边界和右边界时 及时退出
                # res+=diff%n==0?diff/n:diff/n+1 #把剩余的砖块均分了，直接退出
                res += diff / n if diff % n == 0 else diff / n + 1
                return res
            res += 1  # 层数更新
            diff -= (dl + dr + 1)  # 使顶层堆成严格正三角形所需的砖块数(左边所需+右边所需+index处1个)

        return res


print(Solution.maxValue(Solution(), n = 4, index = 2,  maxSum = 6))