class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # rank by frequency -> most frequent
        # cuz we need to process by most frequent first, 
        # so we can fill up the idle time with the other elements and optimise
        # idle time

        # max heap -> while heap has elems loop
        # peek queue and see if time == tuple[1], if true, add curr freq elem to heap
        # from heap pop out most freq elem 
        # increment count and increment time
        # decrement freq elem -1 and if > 0, add it to tuple(freq, time + n)
        # return count
        import heapq
        from collections import deque

        # calc freq
        d = {}
        for t in tasks:
            if t in d:
                d[t] += 1
            else:
                d[t] = 1
        array = list(d.values()) # freq array e.g., [3, 1, 1]
        heap = [-x for x in array]
        heapq.heapify(heap) # max heap [-3, -1, -1]
        q = deque() # queue for checking when idle time is up for a elem
        time, count = 0, 0
        while heap or q:
            time += 1
            if q and q[0][1] == time:
                # add elem back into heap
                heapq.heappush(heap, -q.popleft()[0])
            if len(heap) > 0:
                curr = -heapq.heappop(heap) # negate
                curr -= 1
                if curr > 0:
                    # add back into q + time
                    q.append((curr, time + n + 1))
            count += 1
        return count
        
            

