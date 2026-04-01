class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checkSet = set()
        for i in range(len(nums)):
            checkSet.add(nums[i])
        if len(checkSet) == len(nums):
            return False
        else:
            return True
        