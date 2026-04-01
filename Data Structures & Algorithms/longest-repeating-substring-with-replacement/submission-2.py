class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        check = {}
        # use dictionary
        # aaabaccccb
        l = 0
        max_len = 0
        for r in range(len(s)):

            # add r to dict
            if s[r] not in check:
                check[s[r]] = 1
            else:
                check[s[r]] += 1

            # while the number of replaceable char
            # exceeds k, we need to shift l
            while r - l + 1 - max(check.values()) > k:
                check[s[l]] -= 1
                l += 1
            
            # update max_len
            max_len = max(max_len, r-l+1)
        return max_len

        