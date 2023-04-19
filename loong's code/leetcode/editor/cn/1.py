from typing import List


class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = 'aeiouAEIOU'
        ans = []
        for i in s:
            if i in vowels:
                ans.append(i)
        a = ''
        for i in range(len(s)):
            if s[i] in vowels:
                a += ans.pop()
            else:
                a += s[i]
        return ''.join(a)


print(Solution.reverseVowels(Solution(), s='hello'))


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        start = 0
        end = len(s) - 1
        while start < end:
            while s[end] not in vowels and start < end:
                end -= 1
            while s[start] not in vowels and start < end:
                start += 1
            if s[start] in vowels and s[end] in vowels:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
        return ''.join(s)


print(Solution.reverseVowels(Solution(), s='hallo'))
