class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums, reverse=False) # o(nlogn)
        # -4,-1,-1,0,1,2
        res = []
        for a in range(len(nums)):
            # skip prev identical a
            if a >= 1 and nums[a] == nums[a-1]:
                continue
            # ensure >4 elems are present
            if a + 3 < len(nums):
                for b in range(a + 1, len(nums) - 1):
                    # skip prev identical b
                    if b > a + 1 and nums[b] == nums[b-1]:
                        continue
                    l, r = b + 1, len(nums) - 1
                    while l < r:
                        if target < nums[a] + nums[b] + nums[l] + nums[r]:
                            r -= 1
                        elif target > nums[a] + nums[b] + nums[l] + nums[r]:
                            l += 1
                        else:
                            res.append([nums[a], nums[b], nums[l], nums[r]])
                            l += 1
                            r -= 1
                            # continue sliding l and r if there a duplicate l and r
                            while l < r and nums[l] == nums[l-1] and nums[r] == nums[r+1]:
                                    l += 1
                                    r -= 1
        return res
                        




