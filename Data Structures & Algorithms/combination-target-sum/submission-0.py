class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        # Notice we pass combi as a parameter to avoid global state issues, 
        # though your method of defining it outside works too!
        def dfs(i, current_sum, combi):
            # Base Case 1: We found a valid combination
            if current_sum == target:
                res.append(combi.copy())
                return
            
            # Base Case 2: We overshot the target OR ran out of numbers
            if current_sum > target or i >= len(nums):
                return
            
            # --- CHOICE 1: Include the current number nums[i] ---
            combi.append(nums[i])
            # Recurse, keeping 'i' the same because we can reuse the number
            dfs(i, current_sum + nums[i], combi)
            
            # BACKTRACK: Undo the choice so we can explore the other path
            combi.pop()
            
            # --- CHOICE 2: Skip the current number and move to the next ---
            # We don't add anything to combi or current_sum, just increment i
            dfs(i + 1, current_sum, combi)
            
        dfs(0, 0, [])
        return res