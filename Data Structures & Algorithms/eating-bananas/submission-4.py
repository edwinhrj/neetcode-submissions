class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # start with k = largest value in piles
        # for each p, sum all math.ceil(p / k) 
        # while sum <= h,
        # binary search k by halving it each turn
        # k is from range(1, largest val)
        # while sum <= h
        # binary search by taking it half 
        import math
        l, r = 1, max(piles) # o(n)
        res = r
        while l <= r:
            k = (r + l) // 2
            total_time = 0
            for p in piles:
                total_time += math.ceil(p / k)

            # means rate of eating (k) is v fast, can afford to decrease
            if total_time <= h: 
                res = k # record this speed as valid
                r = k - 1
            # means rate of eating v slow; need speed up rate
            else:
                l = k + 1

        return res