class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        # use a dict -> 
        from collections import defaultdict
        d = defaultdict(int)
        for n in nums: # o(n) space
            d[n] += 1
        for k, v in d.items(): # o(n) time
            if v > len(nums) / 3:
                res.append(k)
        return res