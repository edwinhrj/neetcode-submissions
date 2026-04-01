class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums, reverse=False)
        res = []
        for i in range(len(nums)):
            # skip duplicate i
            if i > 0:
                if nums[i] == nums[i-1]:
                    continue

            # 2 pointer
            # -1, -1, -1, 0, 1, 2, 2, 3
            l, r = i + 1, len(nums) - 1
            while l < r:
                # skip l to next to prev dupl
                if l != i + 1 and nums[l] == nums[l-1]:
                    l += 1
                    continue
                
                # if loop to find valid 3sum
                if nums[i] + nums[l] + nums[r] == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                
        return res
                
# -4,-3,-2,-1,-1,0,0,1,2,3,4
                    
