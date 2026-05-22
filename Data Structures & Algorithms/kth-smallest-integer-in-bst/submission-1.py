# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # go left all the way, then if no more, append to list
        # go right if have
        def dfs(node, res):
            if not node:
                return
            left = dfs(node.left, res)
            res.append(node.val)
            right = dfs(node.right, res)
            return res
        return dfs(root, [])[k-1]
