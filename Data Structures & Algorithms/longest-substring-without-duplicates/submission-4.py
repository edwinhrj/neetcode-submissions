class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check = set()
        max_len = 0
        l = 0
        # we increment r pointer
        for r in range(len(s)):
            # check if r is already in set
            while s[r] in check:
                # if inside alr
                check.remove(s[l]) # remove the LEFT MOST, not r pointer
                l += 1
            
            # if r not in set
            check.add(s[r])
            max_len = max(max_len, len(check))
        return max_len