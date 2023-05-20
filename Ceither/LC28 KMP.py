def strStr(self, haystack: str, needle: str) -> int:
    slow = 0
    fast = len(needle)
    while fast <= len(haystack):
        if haystack[slow:fast] != needle:
            slow += 1
            fast += 1
        else:
            return slow
    return -1