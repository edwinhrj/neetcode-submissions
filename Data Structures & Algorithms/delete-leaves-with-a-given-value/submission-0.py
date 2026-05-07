# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
            if not root:
                return None

            # recurse first
            left, right = root.left, root.right
            self.removeLeafNodes(left, target)
            self.removeLeafNodes(right, target)
            
            # run logic
            if left:
                # check if child is leaf node
                if not left.left and not left.right:
                    if left.val == target:
                        # remove left
                        root.left = None
            if right:
                # check if child is leaf node
                if not right.left and not right.right:
                    if right.val == target:
                        # remove left
                        root.right = None
            
            # last check on root node if it has become a target leaf node
            if not root.left and not root.right and root.val == target:
                return None
            
            return root
            
        
            