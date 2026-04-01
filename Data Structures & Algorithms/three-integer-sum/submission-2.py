class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums, reverse=False )
        res = []

        for i, a in enumerate(nums):
            # if a is currently not the first in the list
            # and is the same as the previous used a,
            # use the next a
            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1

            # 2sum 
            while l < r:
                total = a + nums[l] + nums[r]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    # sum to 0
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    # if next l is the same as previous l, 
                    # move l to the next
                    # NOTE: r will auto move if its the saem
                    # as per the above block
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return res

            
        