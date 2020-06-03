class StockSpanner:
    """#901. Write a class StockSpanner which collects daily price quotes for some stock, 
    and returns the span of that stock's price for the current day.

    The span of the stock's price today is defined as the maximum number of consecutive days 
    (starting from today and going backwards) for which the price of the stock was less than or equal to today's price.
    """

    def __init__(self):
        self.records = []
    
    def next(self, price: int) -> int:
        span = 1
        while self.records and self.records[-1][0] <= price:
            span += self.records.pop()[1]
        self.records.append((price, span))
        return span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
