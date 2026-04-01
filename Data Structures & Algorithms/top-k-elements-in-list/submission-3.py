class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        res = []
        d = defaultdict(int)
        for n in nums:
            d[n] += 1
        # sort dict by count
        d = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
        keys = list(d.keys())
        return keys[:k]

