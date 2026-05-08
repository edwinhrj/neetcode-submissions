class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []
        subset = []

        def dfs(i, subset):

            # base case (when we reached 1 leaf node)
            if i == len(nums):
                res.append(subset.copy())
                return
            
            # left decision (add elem)
            subset.append(nums[i])
            dfs(i + 1, subset)

            # undo choice
            subset.pop()

            # right decision (dont add elem)
            # - do not append
            dfs(i + 1, subset)
        
        dfs(0, subset)
        return res