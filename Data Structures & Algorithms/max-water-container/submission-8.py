class Solution:
    def maxArea(self, h: List[int]) -> int:
        max_area = 0
        for i in range(len(h)):
            for j in range(i, len(h)):
                max_area = max(min(h[i], h[j]) * (j - i), max_area)
        return max_area
