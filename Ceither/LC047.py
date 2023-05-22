def removeDuplicates(self, s: str) -> str:
    li = []
    for i in s:
        li.append(i)
    index = 1
    tempstack = []
    tempstack.append(li[0])
    while index < len(li):
        if len(tempstack) == 0:
            tempstack.append(li[index])
        elif tempstack[-1] == li[index]:
            tempstack.pop()
        else:
            tempstack.append(li[index])
        index += 1
    return ''.join(tempstack)