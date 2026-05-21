# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # bfs
        def bfs(node, res):
            from collections import deque
            q = deque()
            q.append(root)
            while q:
                level = []
                for i in range(len(q)):
                    node = q.popleft()
                    l, r = node.left, node.right
                    if l:
                        level.append(l.val)
                        q.append(l)
                    if r:
                        level.append(r.val)
                        q.append(r)
                if level:
                    res.append(level)
            return res
        
        if root:
            return bfs(root, [[root.val]])
        else:
            return []
                    
                    


