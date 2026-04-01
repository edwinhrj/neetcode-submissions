class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        # len(piles) <= h
        # find largest p and set k as it first
        # min k = 1, max k = max(piles)
        # to keep searching through this (ordered) range, 
        # we can use binary search 
        l, r = 1, max(piles)
        res = 0
        while l <= r:
            k = (l + r) // 2
            # find total time
            total_time = 0
            for p in piles:
                total_time += math.ceil(p / k)
            if total_time <= h:
                # save the best answer now first
                res = k
                # k can be smaller
                r = k - 1
            else:
                # k needs to be larger
                l = k + 1
        return res
            

            



