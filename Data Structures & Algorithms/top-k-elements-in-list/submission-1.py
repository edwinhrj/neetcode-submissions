class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        for num in nums:
            if num not in res:
                res[num] = 1
            else:
                res[num] += 1
        sorted_res = list(sorted(res.items(), key=lambda x: x[1], reverse=True))
        sorted_list = list(map(lambda x: x[0], sorted_res))
        return sorted_list[:k]

        