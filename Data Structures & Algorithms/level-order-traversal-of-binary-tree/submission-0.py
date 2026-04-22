# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # bfs
        from collections import deque

        # edge case when root is null
        if not root:
            return []

        q = deque()
        res = []
        q.append(root)
        res.append([root.val]) # add list(root) to res first
        while q: # while queue has nodes
            lst = []
            for i in range(len(q)):
                curr = q.popleft()
                left, right = curr.left, curr.right
                if left:
                    lst.append(left.val)
                    q.append(left)
                if right:
                    lst.append(right.val)
                    q.append(right)
            if lst:
                res.append(lst)
                
        return res

