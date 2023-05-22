def evalRPN(self, tokens: List[str]) -> int:
    temp = []
    i = 0
    while i < len(tokens):
        if tokens[i][-1].isnumeric():
            temp.append(int(tokens[i]))
        elif tokens[i] == '+':
            a = temp.pop()
            b = temp.pop()
            temp.append(a + b)
        elif tokens[i] == '-':
            a = temp.pop()
            b = temp.pop()
            temp.append(b - a)
        elif tokens[i] == '*':
            a = temp.pop()
            b = temp.pop()
            temp.append(a * b)
        elif tokens[i] == '/':
            a = temp.pop()
            b = temp.pop()
            temp.append(int(b / a))
        i += 1
    return temp[0]