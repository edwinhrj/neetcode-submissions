class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: 
        substring = set()
        max_len = 0
        l = 0

        for r in range(len(s)):
            # while r is a duplicate
            # this will keep looping until l
            # is no longer pointing the duplicated 
            # letter
            while s[r] in substring:
                substring.remove(s[l])
                l += 1
            # add back current r
            substring.add(s[r])
            max_len = max(max_len, len(substring))
        return max_len
