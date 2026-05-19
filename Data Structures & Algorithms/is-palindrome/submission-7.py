class Solution:
        
    def isAlphanum(self, s):
        if (ord('a') <= ord(s) and ord(s) <= ord('z')) or (ord('A') <= ord(s) and ord(s) <= ord('Z')) or (ord('0') <= ord(s) and ord(s) <= ord('9')):
            return True
        else:
            return False

    def isPalindrome(self, s: str) -> bool:
        # 2 pointer
        l, r = 0, len(s) - 1

        # use ord(char) to check if it is a alphanumeric

        while l < r:
            if self.isAlphanum(s[l]):
                if self.isAlphanum(s[r]):
                    if s[l].lower() == s[r].lower():
                        l += 1
                        r -= 1
                        continue
                    else:
                        return False
                else:
                    r -= 1
                    continue
            else:
                l += 1
                continue
        return True