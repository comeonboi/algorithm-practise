def isValid(self, s: str) -> bool:
    li = []
    for i in s:
        li.append(i)
    if len(s) % 2 != 0:
        return False
    tempstack = []
    tempstack.append(li[0])
    index = 1
    while index < len(li):
        if len(tempstack) == 0:
            tempstack.append(li[index])
            index += 1
            continue
        if tempstack[-1] == '(' and li[index] == ')':
            tempstack.pop()
        elif tempstack[-1] == '[' and li[index] == ']':
            tempstack.pop()
        elif tempstack[-1] == '{' and li[index] == '}':
            tempstack.pop()
        else:
            tempstack.append(li[index])
        index += 1
    if len(tempstack) == 0:
        return True
    else:
        return False