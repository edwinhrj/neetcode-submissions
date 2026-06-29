# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # first node is root, consecutive left of root is left branch, 
        # preorder: 1,2,5,3,4  inorder: 5,2,1,3,4
        # 2,5,3,4 and 5,2, 1, 3,4
        # 5,3,4 and 
        
        # build 2 l = none, r = none; recurse call func on l and r, modify arrays etc   
        if not preorder and not inorder:
            return None
        curr = preorder[0]
        root = TreeNode(curr)
        idx = inorder.index(curr)

        root.left = self.buildTree(preorder[1:idx + 1], inorder[:idx])
        root.right = self.buildTree(preorder[idx + 1:], inorder[idx + 1:])

        return root
            
            

