class StockSpanner:

    def __init__(self):
        # append to list
        self.prices = []

    def next(self, price: int) -> int:
        # as you append to list,
        # do a reverse iteration and keep track of len of span
        self.prices.append(price)
        span, pointer, i = 0, self.prices[-1], -1

        # compare prices with the rest of the prices
        while pointer <= price:
            span += 1
            i -= 1
            if abs(i) <= len(self.prices):
                pointer = self.prices[i]
            else:
                break
        
        return span
            




# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)