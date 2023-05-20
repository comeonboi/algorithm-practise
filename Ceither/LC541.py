def reverseStr(self, s: str, k: int) -> str:
    ans = ''
    f = 1
    for i in range(0, len(s), k):
        temp = s[i:i + k]
        f = -f
        ans += temp[::f]
    return ans