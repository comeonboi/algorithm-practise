def halvesAreAlike(s: str) -> bool:
    return sum(c in 'aeiouAEIOU' for c in s[:len(s) >> 1]) == sum(c in 'aeiouAEIOU' for c in s[len(s) >> 1:])


class Solution:
    pass


s = 'textbook'
print(halvesAreAlike(s))
