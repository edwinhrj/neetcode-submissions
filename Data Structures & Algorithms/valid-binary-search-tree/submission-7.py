# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.is_bst = True

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs_helper(node, left_boundary, right_boundary):
            # base case
            if not node:
                return True
            
            # base case
            if node.val >= right_boundary or node.val <= left_boundary:
                return False

            # call recursion
            return dfs_helper(node.left, left_boundary, node.val) and dfs_helper(node.right, node.val, right_boundary)

        return dfs_helper(root, float('-inf'), float('inf'))
            

            