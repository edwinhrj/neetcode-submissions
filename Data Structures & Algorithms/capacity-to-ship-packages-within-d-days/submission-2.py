class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # start off with sum of all elems as weight capacity
        # binary search range(0, w_c)
        # at each m, while curr_days < days, iterate thru + sum and fill up to <= w_c
        # increment curr_days += 1
        # update w_c

        l, r = max(weights), sum(weights)
        min_wc = r

        while l <= r:
            m, curr_days, packed = ((l + r) // 2), 1, 0

            # find way to pack elems together within limit m,
            # then reset to go on to packing next elems

            for w in weights:
                if packed + w > m:
                    curr_days += 1
                    packed = 0 # reset to continue packing next few elems
                packed += w
            
            if curr_days <= days:
                # save current min_wc
                min_wc = min(min_wc, m)
                # can afford to decrease m
                r = m - 1
            
            else:
                # need to increase m since overshoot days
                l = m + 1
        
        return min_wc
            

                