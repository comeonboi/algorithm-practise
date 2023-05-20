def reverseWords(self, s: str) -> str:
    # ans = ''
    # s = s.strip().split(' ')
    # index = 0
    # while index < len(s):
    #     if not s[index].isalnum():
    #         s.remove(s[index])
    #         index -= 1
    #     index += 1
    # for i in range(1, len(s)+1):
    #     if i != len(s):
    #         ans += s[-i]
    #         ans += ' '
    #     else:
    #         ans += s[-i]
    # return ans

    return ' '.join(s.split()[::-1])