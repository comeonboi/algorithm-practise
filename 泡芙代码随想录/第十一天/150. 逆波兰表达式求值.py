class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] == "+":
                stack = stack[:-2]+[stack[-2]+stack[-1]]
            elif tokens[i] == "-":
                stack = stack[:-2]+[stack[-2]-stack[-1]]
            elif tokens[i] == "*":
                stack = stack[:-2]+[stack[-2]*stack[-1]]
            elif tokens[i] == "/":
                stack = stack[:-2]+[int(stack[-2]/stack[-1])]
            else:
                stack.append(int(tokens[i]))
        print(stack)
        return stack[-1]