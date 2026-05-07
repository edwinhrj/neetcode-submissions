class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        import heapq
        heap = []
        # o(n)
        for num in arr:
            heapq.heappush(heap, (-abs(num - x), -num)) # max_heap of (-diff, -num)
            while len(heap) > k:
                heapq.heappop(heap) # pops out the largest diff to x, then smallest num if tie breaker
        
        heap = [-x[1] for x in heap] # extract out the k + 1 closest num o(k)

        return sorted(heap) # o(klogk)
        
        # overall time complexity is o(nlogk) 

        