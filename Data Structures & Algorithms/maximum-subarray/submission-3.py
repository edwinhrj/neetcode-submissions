class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # greedy
        # curr sum = 0
        # as we loop thru nums, if n + sum > 0, we keep n
        # if n + sum < 0, we reset cursum = 0
        # at each point we take the max(currsum, max_sum)
        max_sum, curr_sum = nums[0], nums[0]
        if len(nums) > 1:
            for n in nums[1:]:
                if n + curr_sum > 0:
                    curr_sum += n
                    max_sum = max(max_sum, curr_sum)
                else:
                    curr_sum = 0
                    max_sum = max(max_sum, n)

        return max_sum

