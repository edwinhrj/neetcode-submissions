# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # bfs -> level order of nodes in list
        # for each level -> index the -1 node

        def bfs(node):
            from collections import deque
            q = deque()

            q.append(node)
            res = []
            # edge case empty tree
            if root:
                res.append(root.val)
            else:
                return res
                
            while q:
                level = []
                for i in range(len(q)):
                    curr = q.popleft()
                    if curr.left:
                        level.append(curr.left.val)
                        q.append(curr.left)
                    if curr.right:
                        level.append(curr.right.val)
                        q.append(curr.right)
                # add right most node at every level
                if level:
                    res.append(level[-1])
            return res

        return bfs(root)


                
                

