class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # sliding window 
        if len(nums) == 1:
            if nums[0] >= target:
                return 1
            else:
                return 0

        l, min_len, check = 0, len(nums), False
        summ = 0
        for r in range(len(nums)):
            summ += nums[r]
            while summ >= target:
                check = True
                # store min_len
                min_len = min(min_len, r - l + 1)
                summ -= nums[l]
                l += 1
        return min_len if check else 0
            
            
            