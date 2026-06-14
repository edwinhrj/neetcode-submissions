class Solution:
    def pacificAtlantic(self, grid: List[List[int]]) -> List[List[int]]:
        # visited is my result
        # multi source bfs for all pacific + atlantic -> 
        # return list(res)
        import collections
        atl, pac, res = collections.deque(), collections.deque(), []
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if r == 0 or c == 0:
                    pac.append((r, c))
                if r == len(grid) - 1 or c == len(grid[0]) - 1:
                    atl.append((r, c))
        
        def bfs(q):
            visited = set(q)
            while q:
                curr = q.popleft()
                directions = [[0, 1], [0,-1], [1,0], [-1,0]]
                for d in directions:
                    # boundaries
                    if curr[0] + d[0] < len(grid) and curr[0] + d[0] >= 0 and curr[1] + d[1] < len(grid[0]) and curr[1] + d[1] >= 0 and (curr[0] + d[0], curr[1] + d[1]) not in visited:
                        if grid[curr[0] + d[0]][curr[1] + d[1]] >= grid[curr[0]][curr[1]]:
                            q.append((curr[0] + d[0], curr[1] + d[1]))
                            visited.add((curr[0] + d[0], curr[1] + d[1]))
            return visited
        
        atl, pac = bfs(atl), bfs(pac)
        for p in atl:
            if p in pac:
                res.append(p)
        return res
