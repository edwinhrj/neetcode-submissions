class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                first, second = nums[i], nums[j]
                if i != j and (first + second) == target:
                    res.append(i)
                    res.append(j)
                    res.sort()
                    return res
        