class Solution:
    def maxArea(self, h: List[int]) -> int:
        max_area = 0
        l, r = 0 , len(h) - 1
        while l < r:
            max_area = max(max_area, min(h[l], h[r]) * (r - l))

            # if l is shorter than r, shift l to find taller
            if h[l] < h[r]:
                l += 1
            else:
                r -= 1
        return max_area
