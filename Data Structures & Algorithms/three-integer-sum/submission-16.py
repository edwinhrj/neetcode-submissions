class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort first, then iterate thru then use 2 pointer

        nums = sorted(nums, reverse=False)

        res = []
        for i in range(len(nums)):
            if i > 0:
                if nums[i] == nums[i - 1]:
                    continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                    continue
                else:
                    l += 1
                    continue
        return res
                