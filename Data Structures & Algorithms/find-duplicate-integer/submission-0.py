class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ndict = {}
        for n in nums:
            if n in ndict:
                ndict[n] += 1
            else:
                ndict[n] = 1
        sortedList = list(sorted(ndict.items(), key=lambda x: x[1], reverse=True))
        return sortedList[0][0]
        