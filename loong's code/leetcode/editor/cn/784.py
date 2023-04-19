from collections import deque

def letterCasePermutation(s):
    string = []
    q = deque([''])
    while q:
        cur = q[0]
        pos = len(cur)
        if pos == len(s):
            string.append(cur)
            q.popleft()
        else:
            if s[pos].isalpha():
                q.append(cur + s[pos].swapcase())
            q[0] += s[pos]
    return string

s = input()
print(letterCasePermutation(s))
