class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums, reverse=False)

        unique = set(nums)
        # now unique will be 2,3,4,5,10,20

        # to do checking in a simple way
        # without 2 pointer
        max_length = 0
        for num in nums:
            count = 0
            if num - 1 not in nums:
                count += 1
                while num + 1 in nums:
                    count += 1
                    num += 1
                max_length = max(count, max_length)
        return max_length