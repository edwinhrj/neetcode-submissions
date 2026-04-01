class Solution:
    def maxArea(self, h: List[int]) -> int:
        l, r = 0, len(h) - 1
        largest_vol = 0
        while l < r:
            largest_vol = max(largest_vol, min(h[l], h[r])*(r - l))
            if h[l] <= h[r]:
                l += 1
            else:
                r -= 1
        return largest_vol