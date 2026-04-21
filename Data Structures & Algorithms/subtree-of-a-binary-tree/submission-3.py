# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        # helper dfs to compare each root with unchanging subroot
        def isSameTree(tree1, tree2=subRoot):
            if tree1 == None and tree2 == None:
                return True

            if tree1 and tree2 and tree1.val == tree2.val:
                return isSameTree(tree1.left, tree2.left) and isSameTree(tree1.right, tree2.right)
            
            return False

        
        # main dfs through root
        if root != None:
            if isSameTree(root):
                return True
            else:
                return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        else:
            return False
        # find a way to account for when root is null

        


            
            
            
            

            
        
        

        

        