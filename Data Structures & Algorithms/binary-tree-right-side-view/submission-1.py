# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # bfs to keep track of level
        # in each level, only append the right most node into res; stack is used

        from collections import deque
        q = deque()
        res = []
        
        # edge case when root is null
        if not root:
            return res
        
        q.append(root)
        res.append(root.val) # append root first

        while q:
            stack = []
            for node in range(len(q)):
                curr = q.popleft()
                left, right = curr.left, curr.right
                if left:
                    stack.append(left.val)
                    q.append(left)
                if right:
                    stack.append(right.val)
                    q.append(right)
            if stack:
                res.append(stack.pop())
        return res


                


        