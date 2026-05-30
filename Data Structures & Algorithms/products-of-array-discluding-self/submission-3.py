class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # multiply everything into array of size n
        # iterate thru nums and array and divide
        # 2*4*6, 4*6, 6, 

        res = []
        for i in range(len(nums)):
            prod = 1
            for j in range(len(nums)):
                if i != j:
                    prod *= nums[j]
            res.append(prod)
        return res