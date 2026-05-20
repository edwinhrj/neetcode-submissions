class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window algo
        # as we slide we will add it to
        # a dict
        from collections import defaultdict
        d = defaultdict(int)
        l, max_len = 0, 0
        for r in range(len(s)):
            # add s[r] to d
            d[s[r]] += 1
            
            # while least freqe char is more than k, 
            # need to incrementing l and removing
            # AAABCBB k = 2
            while r - l + 1 - max(list((d.values()))) > k:
                d[s[l]] -= 1 # remove curr l
                l += 1 # increment left pointer
            max_len = max(max_len, r - l + 1)
        return max_len

        