# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # if curr.val is bigger than p and q, return curr.left
        # if curr.val is smaller than p and q, return curr.right
        # base cases
        if root.val == p.val:
            return root
        if root.val == q.val:
            return root
        if root.val < p.val and q.val < root.val:
            return root
        if root.val < q.val and p.val < root.val:
            return root

        # recurse
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        

        
        
        