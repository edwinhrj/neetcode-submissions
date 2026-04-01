class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_len = 0
        l = 0
        for r in range(len(s)):
            # add r to count
            if s[r] in count:
                count[s[r]] += 1
            else:
                count[s[r]] = 1
            
            # while length of window - number of most frequent char
            # is more than k, the current substring is invalid
            # thus, we increment l
            while (r - l + 1) - max(count.values()) > k:
                # remove l from count
                count[s[l]] -= 1

                # increment l
                l += 1
            
            # once r is incremented, and the k is not exceeded,
            # we will update max_len 
            max_len = max(max_len, (r - l + 1))
        
        return max_len