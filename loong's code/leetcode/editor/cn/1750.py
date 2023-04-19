class Solution:
    def minimumLength(self, s: str) -> int:
        start = 0
        tail = len(s) - 1
        while start < tail and s[start] == s[tail]:
            c = s[start]
            while start <= tail and s[start] == c:
                start += 1
            while start <= tail and s[tail] == c:
                tail -= 1
        return tail-start + 1

