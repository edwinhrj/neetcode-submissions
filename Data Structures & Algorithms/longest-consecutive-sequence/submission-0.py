class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        max_len = 0
        for num in numSet:
            length = 0
            # first of the sequence
            if (num - 1) not in numSet:
                length += 1
                while (num + 1) in numSet:
                    length += 1
                    num += 1
            max_len = max(length, max_len)
        return max_len
