class KthLargest:
    # use a heap structure

    def __init__(self, k: int, nums: List[int]):
        import heapq
        heapq.heapify(nums) # min heap
        self.k = k
        self.heap = nums

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
        
        
