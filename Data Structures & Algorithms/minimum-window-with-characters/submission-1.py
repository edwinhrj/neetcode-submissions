class Solution:
    def isValid(self, d1, d2):
        for k in d1.keys():
            if d1[k] < d2[k]:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        # use a hashmap to store t
        # use a identical key hashmap to store curr substring 
        # use a sliding window, updating min length of substring each iteration
        # once 
        # "OUZYYYYDYXAZVXYYZ", t = "XYYZ"
        # return YDYXAZ
        from collections import defaultdict
        l, t_dict, s_dict, res, found = 0, defaultdict(int), defaultdict(int), s, False
        for n in t:
            t_dict[n] += 1
            s_dict[n] = 0
        for r in range(len(s)):
            if s[r] in s_dict.keys():
                s_dict[s[r]] += 1
            while self.isValid(s_dict, t_dict): # find a way to check if all values in s_dict are >= t_dict
                found = True
                if len(res) >= len(s[l: r + 1]):
                    res = s[l: r + 1] # upd shortest substring
                # remove s[l]
                if s[l] in s_dict.keys():
                    s_dict[s[l]] -= 1
                # move l to next
                l += 1
            
        return res if found else ""
