class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # iterate thru each elem and append to stack
        # if num is a arithmentic, keep popping while stack has elems
        # apply the given arithmetic to the elems (2 popped from stack)
        # return stack[0]

        stack = []
        for n in tokens:
            if n in ['+', '-', '*', '/']:
                second = int(stack.pop())
                first = int(stack.pop())
                if n == '+':
                    stack.append(first + second)
                if n == '-':
                    stack.append(first - second)
                if n == '*':
                    stack.append(first * second)
                if n == '/':
                    stack.append(int(first / second))
            else:
                stack.append(int(n))
        return stack[0]
