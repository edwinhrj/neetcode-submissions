class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # use heap for optimized o(klogk) time
        # get first k elements and heapify o(log k)
        # while len(heap) > k, heappop
        # push the rest of the elems into heap
        # return heap

        import heapq
        heap = []
        for p in points:
            # extract into (dist, [x, y])
            point = (-1*(p[0]**2 + p[1]**2), p)

            heapq.heappush(heap, point) # max heap
            while len(heap) > k:
                # pop the largest (which we dont want)
                heapq.heappop(heap)
            
        res = []
        for h in heap:
            res.append(h[1])
        return res





        