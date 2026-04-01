class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        # [-4, -1, -1, 0, 1, 2]
        res = []
        for i in range(len(nums)):
            # check for same i as before
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                triplets = []
                total = nums[i] + nums[l] + nums[r]
                if total == 0:
                    triplets.append(nums[i])
                    triplets.append(nums[l])
                    triplets.append(nums[r])
                    if triplets not in res:
                        res.append(triplets)
                    l += 1
                elif total < 0:
                    l += 1
                else:
                    r -= 1
        return res