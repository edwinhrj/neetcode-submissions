class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 2 pointer
        l = 0
        res = []
        while l < len(nums):
            r = 0
            product = 1
            while r < len(nums):
                if r != l:
                    product *= nums[r]
                r += 1
            res.append(product)
            l += 1
        return res

