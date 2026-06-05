class Solution:
    def simplifyPath(self, path: str) -> str:
        stack, start, word, res = [], True, "", ""
        if path[-1] != "/":
            path += "/"

        for char in path:
            if char == "/":
                if start:
                    if word == "..":
                        # pop from stack
                        if stack:
                            stack.pop()
                        word, start = "", False
                    elif word == "." or word == "":
                        word, start = "", False
                        continue
                    else:
                        stack.append(word)
                        word, start = "", False
            else: 
                start = True
                word += char
        
        for w in stack:
            res += "/"
            res += w
        
        if not stack:
            res += "/"
        
        return res


