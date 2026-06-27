# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # do a bfs and keep track of count each time
        # process all nodes in each level instead of one by one
        # use len(q) to aid in processing all nodes in each level
        # do 1 level bfs, max_count += 1
        if root == None:
            return 0

        from collections import deque
        q = deque()
        q.append(root)
        visited = set()
        visited.add(root)

        h = 0

        while q:
            nodes_in_level = len(q)
            for i in range(nodes_in_level):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            h += 1
        return h
                    

        