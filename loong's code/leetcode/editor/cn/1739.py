class Solution:
    def minimumBoxes(self, n: int) -> int:
        cur = i = j = 1
        while n > cur:
            n -= cur
            i += 1
            cur += i
        cur = 1
        while n > cur:
            n -= cur
            j += 1
            cur += 1
        return (i - 1) * i // 2 + j
