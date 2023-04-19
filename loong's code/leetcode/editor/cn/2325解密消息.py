from string import ascii_lowercase

class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        str1 = ''
        dict1 = {}
        index = 0
        for i in key.replace(' ', ''):
            if i not in dict1:
                dict1[i] = ascii_lowercase[index]
                index += 1
        for i in message:
            if i in dict1:
                str1 += dict1[i]
            else:
                str1 += ' '
        return str1

print(Solution.decodeMessage(Solution(), key="the quick brown fox jumps over the lazy dog", message="vkbs bs t suepuv"))
