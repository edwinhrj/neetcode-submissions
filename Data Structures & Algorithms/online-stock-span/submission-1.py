class StockSpanner:

    def __init__(self):
        self.prices = [] # store (price, span)

    def next(self, price: int) -> int:
        # to do this problem in o(n) time, store pair(price, span)
        # in a stack
        # we can keep popping out the end elem and if curr price is greater then
        # the curr one, means it will also be greater the rest of the elems in
        # that span, so can js sum the span of all the prices that curr is larger than
        # to get curr's span
        # then we can js pop out the smaller prices and append the curr one 
        # since we dont need historical prices, js need to store the span


        span = 1
        while self.prices and self.prices[-1][0] <= price:
            # while end elem is smaller then curr, sum its span 
            # and pop it and move on to next to check again
            span += self.prices[-1][1]
            self.prices.pop() # remove end elem that is smallest
        self.prices.append((price, span))
        
        return span
            




# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)