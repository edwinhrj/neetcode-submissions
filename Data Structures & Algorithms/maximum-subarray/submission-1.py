class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # use kadane's algorithm
        # start w first elem as curSum, maxSum
        # iterate thru list from idx=1, if prev running total is -,
        # drop prev total, and start w current n

        currSum, maxSum = nums[0], nums[0]

        for n in nums[1:]:
            if currSum < 0:
                currSum = n
            else:
                currSum += n
            maxSum = max(maxSum, currSum)
        return maxSum