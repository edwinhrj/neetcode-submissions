class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def dfs(sol, res):
            # base case
            if len(sol) == len(nums):
                res.append(sol.copy())
                return
            
            # decision 1: go thru nums and add first num that is not alr in sol
            for n in nums:
                if n not in sol:
                    sol.append(n)
                    dfs(sol, res) # recurse here
                    sol.pop()
            
            return res
        return dfs([], [])

