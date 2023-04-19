if 1:
    if 1:
        expression = "!(&(&(f),&(!(t),&(f),|(f)),&(!(&(f)),&(t),|(f,f,t))))"
        stack = []
        # 存地址
        address = []
        address2 = []
        # 我其实是地址
        flag = 0
        # 地址
        return_s = 2
        for i in expression:
            if i == '(':
                flag = expression.find("(", flag)
                address.append(flag)
                stack.append("(")
            if i == ')':
                flag_t = 0
                flag_f = 0
                # 找到了最近的左括号address[-1],中间夹的：
                for j in expression[address[-1]+1:flag].split(","):
                    if j == 't':
                        flag_t += 1
                        return_s = 1
                    if j == 'f':
                        flag_f += 1
                        return_s = 0
                if expression[address[-1] - 1] == "&":
                    if flag_t > 0 and flag_f > 0:
                        return_s = 0
                    if flag_t > 0 and flag_f == 0:
                        return_s = 1
                elif expression[address[-1] - 1] == '!':
                    if return_s == 0:
                        return_s = 1
                    else:
                        return_s = 0
                elif expression[address[-1] - 1] == '|':
                    if flag_t > 0:
                        return_s = 1
                stack.pop()
                if return_s == 1:
                    expression = expression.replace(expression[address[-1] - 1:flag+1], "t")
                    flag -= flag + 1 - address[-1]
                else:
                    expression = expression.replace(expression[address[-1] - 1:flag+1], "f")
                    flag -= flag + 1 - address[-1]
                address.pop()
            flag += 1
        print(bool(return_s))

