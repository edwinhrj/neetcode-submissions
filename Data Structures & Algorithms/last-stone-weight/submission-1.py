class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # heapify array to max array
        # while array: largest pop, peep next and if smaller, - off and push into heap
        # 6,4,3,2,2

        import heapq
        stones = [-x for x in stones]
        heapq.heapify(stones) # max heap
        while stones:
            largest = -heapq.heappop(stones)
            if stones:
                nxt = -heapq.heappop(stones)
                if nxt < largest:
                    heapq.heappush(stones, -(largest - nxt))
            else:
                return largest
        return 0


        