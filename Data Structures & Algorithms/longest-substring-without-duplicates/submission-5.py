class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        check = set()
        # as you slide, if char not in set, add it and upd max length
        # if in set, remove l and slide l to right

        l = 0
        for r in range(l, len(s)):
            while s[r] in check:
                check.remove(s[l])
                l += 1
            if s[r] not in check:
                check.add(s[r])
                max_len = max(max_len, len(check))
        return max_len