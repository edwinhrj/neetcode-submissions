class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # sliding window
        max_profit, l = 0, 0
        for r in range(len(prices)):
            while prices[r] < prices[l]:
                l = r
            max_profit = max(max_profit, prices[r] - prices[l])
        return max_profit