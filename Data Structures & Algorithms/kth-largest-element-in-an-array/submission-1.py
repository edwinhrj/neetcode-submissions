class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # o(nlogk) time
        # heapify array -> o(n)
        # insert into k sized array -> o(logk)
        # go thru all n elems and insert into array -> o(nlogk)
        # pop out all the smallest elems, leaving top k largest in aray
        # kth largest will be array[0]

        import heapq
        heap = []
        for n in nums:
            heapq.heappush(heap, n)
            while len(heap) > k:
                heapq.heappop(heap)
        return heap[0]
        
        