class Solution:

    def isPalindrome(self, s: str) -> bool:

        def isAlphaNum(c):
            return ord('A') <= ord(c) <= ord('Z') or ord('a') <= ord(c) <= ord('z') or ord('0') <= ord(c) <= ord('9')

        l, r = 0, len(s) - 1
        while l < r:
            if not isAlphaNum(s[l]):
                l += 1
                continue
            if not isAlphaNum(s[r]):
                r -= 1
                continue
            if s[l].lower() == s[r].lower():
                l, r = l + 1, r - 1
                continue
            else:
                return False
        return True
            


        
        