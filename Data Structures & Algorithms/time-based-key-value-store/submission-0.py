class TimeMap:
    from collections import defaultdict

    def __init__(self):
        self.store = defaultdict(list)
        # timestamp will be added in increasing order
        # {alice: [(happy, 1), (sad, 3)], betty: []}
        # 0,1.6.10.40.56

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))

    def get(self, key: str, target: int) -> str:
        # check if structure is len() >= 1
        # AND check prev_timestamp is <= timestamp
        
        # since timestamp added in increasing order, use binary
        # search to hit o(log n) time
        res = ""
        lst = self.store[key]
        l, r = 0,len(lst) - 1
        while l <= r:
            m = (l + r) // 2
            if target < lst[m][1]:
                r = m - 1
            else:
                res = lst[m][0]
                l = m + 1
        return res
                