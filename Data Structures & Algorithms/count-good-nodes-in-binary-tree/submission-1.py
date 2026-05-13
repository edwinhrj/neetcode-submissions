# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.count = 0

    def goodNodes(self, root: TreeNode) -> int:
        # dfs helper, take in node + currLargestNode val
        # at every level, update currLargestNode and if > node, count += 1

        def dfs(node, currLargestNode):
            if not node:
                return
            
            if currLargestNode.val <= node.val:
                self.count += 1
            
            if node.left:
                if node.left.val > currLargestNode.val:
                    dfs(node.left, node.left)
                else:
                    dfs(node.left, currLargestNode)
            else:
                dfs(node.left, currLargestNode)
                
            if node.right:
                if node.right.val > currLargestNode.val:
                    dfs(node.right, node.right)
                else:
                    dfs(node.right, currLargestNode)
            else:
                dfs(node.right, currLargestNode)
        dfs(root, root)
        return self.count

        




        