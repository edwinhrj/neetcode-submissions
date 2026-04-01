class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # only can iterate thru once o(n)
        # use dictionary
        count = {}
        for letter in nums:
            if letter in count:
                count[letter] += 1
            else:
                count[letter] = 0
                count[letter] += 1

            
        # sort dictionary by value, ascending = false
        # looks like [(3, 700), (2, 600), (2, 30)]
        count = sorted(list(count.items()), key=lambda x: x[1], reverse=True)
        keys = count[0:k]
        res = []
        for pair in keys:
            res.append(pair[0])
        return res
        