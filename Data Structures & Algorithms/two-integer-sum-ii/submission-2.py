class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 2 pointer
        l, r = 0, len(nums) - 1
        res = []
        while l < r:
            curr = nums[l] + nums[r]
            if curr < target:
                l += 1
            elif curr > target:
                r -= 1
            else:
                res.append(l + 1)
                res.append(r + 1)
                break
        return res

            
        