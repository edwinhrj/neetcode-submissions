class Solution:
    def helper(self, s, k):
        s, k = s[::-1], k[::-1] # reverse list
        k = int("".join(k))
        return s*k

    def decodeString(self, s: str) -> str:
        integer = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        stack = []
        for char in s:
            if char == ']':
                pop = stack.pop()
                encoded, k = [], []
                while pop != '[':
                    encoded.append(pop)
                    pop = stack.pop()
                # continue pop the next one to get integer
                peek = stack[-1]
                while peek in integer:
                    k.append(peek)
                    stack.pop()
                    if stack:
                        peek = stack[-1]
                    else:
                        break
                
                # add back decoded string
                stack.extend(self.helper(encoded, k))

            else:
                stack.append(char)
        
        return "".join(stack)









        
        