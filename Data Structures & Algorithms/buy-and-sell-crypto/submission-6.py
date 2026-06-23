class Solution:
    def maxProfit(self, p: List[int]) -> int:
        l = 0
        max_profit = 0
        for r in range(len(p)):
            if r == l:
                continue
            if p[r] < p[l]:
                l = r
            max_profit = max(p[r] - p[l], max_profit)

        return max_profit
            





        