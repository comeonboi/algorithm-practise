class Solution:
    def countDigitOne(self, n: int) -> int:
        mulk = 1
        ans = 0
        while n >= mulk:
            ans += (n // (mulk * 10)) * mulk + min(max(n % (mulk * 10) - mulk + 1, 0), mulk)
            mulk *= 10
        return ans


print(Solution.countDigitOne(Solution(), n=12))
