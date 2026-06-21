class MedianFinder:
    # 1,5,6,3,4
    # split data stream into 2 halves for fast computation of median
    # use max heap for smaller half and min heap for larger half
    # enforce len(smaller_half) - len(larger_half) <= 1
    # every addNum, if  <= num <= 
    # 1,2,3,4  100,101,102
    # 5

    def __init__(self):
        import heapq
        self.smaller_half = []
        self.larger_half = []
        self.length = 0
        
    def addNum(self, num: int) -> None:
        # logic is to add to smaller heap, then pop out the largest of the smallest
        # then add to larger half -> ensures wtv we add to larger
        # then carry out rebalancing by ensuring smaller half - larger half <= 1
        heapq.heappush(self.smaller_half, -num)
        temp = -heapq.heappop(self.smaller_half)
        heapq.heappush(self.larger_half, temp)

        if len(self.smaller_half) < len(self.larger_half):
            # rebalance
            temp = heapq.heappop(self.larger_half)
            heapq.heappush(self.smaller_half, -temp)
        
        self.length += 1
    


    def findMedian(self) -> float:
        if self.isOdd():
            return -self.smaller_half[0]
        return (self.larger_half[0] + -self.smaller_half[0]) / 2
        

    def isOdd(self) -> bool:
        if self.length % 2 == 0:
            return False
        return True

        