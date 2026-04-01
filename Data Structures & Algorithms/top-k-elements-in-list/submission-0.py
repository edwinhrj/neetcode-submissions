class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
        items_sorted = list(sorted(count.items(), key=lambda x: x[1], reverse=True))[:k]
        value_sorted = list(map(lambda x: x[0], items_sorted))
        return value_sorted