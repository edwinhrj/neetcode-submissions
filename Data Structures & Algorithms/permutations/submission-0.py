class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(path, used):
            # Base Case: We've used all the numbers, so we have a valid permutation.
            if len(path) == len(nums):
                # We must append a COPY of the path (path[:]), 
                # because the original 'path' list will be modified later.
                res.append(path[:]) 
                return
            
            # Loop through all possible numbers we can add
            for i in range(len(nums)):
                # Skip numbers we are already using in the current permutation
                if used[i]:
                    continue
                
                # 1. Make a choice
                path.append(nums[i])
                used[i] = True
                
                # 2. Explore down that path
                backtrack(path, used)
                
                # 3. Undo the choice (Backtrack) so we can try the next number
                path.pop()
                used[i] = False
                
        # Start the recursion with an empty path and no used numbers
        backtrack([], [False] * len(nums))
        
        return res