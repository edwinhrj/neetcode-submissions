class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        combi = []
        
        def dfs(i, current_sum, target):

            # base case 1
            if current_sum == target:
                res.append(combi.copy())
                return
            
            # base case 2 if overshoot target or i >= > len(nums) just return
            if current_sum > target or i >= len(nums):
                return
            
            # choice 1 keep adding same i 
            combi.append(nums[i])
            dfs(i, current_sum + nums[i], target)

            # backtrack if hit any of the base cases
            combi.pop()

            # choice 2: stop looking at curr i and look at next i
            dfs(i + 1, current_sum, target)

        dfs(0, 0, target)
        return res