class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for s in tokens:
            if s in ['+', '-', '*', '/']:
                if s == '+':
                    res = stack.pop() + stack.pop()
                    stack.append(res)
                if s == '-':
                    first = stack.pop()
                    second = stack.pop()
                    res = second - first
                    stack.append(res)
                if s == '*':
                    res = stack.pop() * stack.pop()
                    stack.append(res)
                if s == '/':
                    first = stack.pop()
                    second = stack.pop()
                    res = int(second / first)
                    stack.append(res)
            else:
                stack.append(int(s))
        return stack.pop()
        