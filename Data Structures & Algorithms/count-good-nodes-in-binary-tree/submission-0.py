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

        def dfs(root, currLargestNode):
            # dfs helper, but pass in value of curr largest node
            # and keep updating it every recurse. if curr =< largest_node,
            # increment count
            if not root:
                return 

            if root.val >=  currLargestNode.val:
                self.count += 1
            
            # if next node is larger than curr, update currLargestNode
            if root.left:
                dfs(root.left, root.left if currLargestNode.val <= root.left.val else currLargestNode) 
            if root.right:
                dfs(root.right, root.right if currLargestNode.val <= root.right.val else currLargestNode) 
        
        # call helper
        dfs(root, root)
        
        return self.count

        




        