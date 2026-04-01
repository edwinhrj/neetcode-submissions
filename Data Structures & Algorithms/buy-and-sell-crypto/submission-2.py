class Solution:
    def maxProfit(self, p: List[int]) -> int:
        max_profit = 0
        l, r = 0, 1

        while l < len(p) and r < len(p):
            while r < len(p) and p[r] <= p[l]:
                l = r
                r += 1
                if r >= len(p):
                    break
            # 10, 5, 3, 1, 1, 5, 6, 7, 1
            
            if r >= len(p):
                    break
            max_profit = max(max_profit, p[r] - p[l])
            # shift r 
            r += 1
        return max_profit

            





        