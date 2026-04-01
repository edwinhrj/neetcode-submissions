class Solution:

    def isPalindrome(self, s: str) -> bool:
        def isAlphanumeric(char):
            return ord('a') <= ord(char) <= ord('z') or ord('0') <= ord(char) <= ord('9')
        
        s = s.lower()
        l, r = 0, len(s) - 1
        while l < r:
            if not isAlphanumeric(s[l]):
                l += 1
                continue
            if not isAlphanumeric(s[r]):
                r -= 1
                continue
            if s[l] != s[r]:
                return False
            else:
                l += 1
                r -= 1
        return True
        
        