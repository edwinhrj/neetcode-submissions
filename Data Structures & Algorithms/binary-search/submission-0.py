class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        # <= instead of normal 2 pointer < because we 
        # want to continue the logic even if both l and r 
        # are landing on the same number
        while l <= r: 
            m = (l + r) // 2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1