class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # empty min heap, push k elements in # o(k log k)
        # as we go thru n elems, time will be o(nlogk)

        import heapq
        heap = []

        for n in nums:
            heapq.heappush(heap, n)

            while len(heap) > k:
                heapq.heappop(heap) # pop out the smallest elem till only k elems in
                
        return heap[0]
        