class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        nums = sorted(nums, reverse=False)
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1

        # sliding window to count len >= 2 cases
        l = 0
        max_len = 1
        for r in range(1, len(nums)):
            if r != l and nums[r] - nums[r - 1] == 1:
                max_len = max(max_len, r - l + 1)
            while r != l and nums[r] - nums[r - 1] != 1:
                l += 1
        return max_len

                
