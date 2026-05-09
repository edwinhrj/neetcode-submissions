class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # backtracking all possible combinations
        # CONSTRAINT: can only choose 1 elem in each combi
        # turn 

        # 1,4,2,5,2,6,9
        # 1,2,5

        # if i sort candidates first,
        # 1,2,2,4,5,6,9 -> o(nlogn)

        candidates = sorted(candidates, reverse=False) # o(nlogn)
        res = []
        def dfs(i, current_sum, combi, target):
            # base cases
            if current_sum == target:
                res.append(combi.copy())
                return # ends current track 
            if current_sum > target or i >= len(candidates):
                # overshoot so we backtrack
                return
            
            # choice 1: keep adding next candidates[i] to current_sum
            combi.append(candidates[i])
            dfs(i + 1, current_sum + candidates[i], combi, target)

            # backtrack by 1 elem if base case reached
            combi.pop()

            # choice 2: skip next elem, and go to next elem that is not repeated (since 
            # array is sorted we can do this)
            next_i = i + 1
            while next_i < len(candidates) and candidates[next_i] == candidates[i]:
                next_i += 1
            dfs(next_i, current_sum, combi, target)

        dfs(0, 0, [], target)
        return res



        