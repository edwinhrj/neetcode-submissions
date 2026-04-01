# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0 # global variable 

        # do a dfs to get the height of tree
        def dfs(curr):
            # base case
            if not curr:
                return 0
            
            left = dfs(curr.left)
            right = dfs(curr.right)
            self.res = max(self.res, left + right)
            
            return max(left, right) + 1
        
        dfs(root) # call the function

        return self.res
        
        
        
        