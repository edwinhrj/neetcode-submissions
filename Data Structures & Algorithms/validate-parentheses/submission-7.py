class Solution:
    def isValid(self, s: str) -> bool:
        # iterate thru string
        # if open -> add to stack
        # if close -> pop out from stack and if .pop corresponds to curr
        # continue, if not return false

        stack = []
        check = {'(':')', '{':'}', '[':']'}
        bool_flag = False
        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
                bool_flag = False
            else:
                if len(stack) > 0:
                    top = stack.pop()
                    if check[top] == c:
                        bool_flag = True
                    else:
                        return False
                else:
                    return False
        if len(stack) > 0:
            return False
        else:
            return bool_flag

        