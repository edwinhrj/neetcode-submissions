# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # recursion, every node you swap left and right child 

        # base case
        if root == None:
            return root
        
        # swap
        temp = root.right
        root.right = root.left
        root.left = temp

        # call recursion IN PLACE!!
        self.invertTree(root.left)
        self.invertTree(root.right)

        # when root is returned, its still 
        # pointing to the original root node
        return root 
        
        