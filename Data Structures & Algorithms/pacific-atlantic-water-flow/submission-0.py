class Solution:
    def pacificAtlantic(self, grid: List[List[int]]) -> List[List[int]]:
        # form 2 lists of pacific and atlantic points first 
        # for each point in grid, do a bfs -> check if popped point is in atlantic or pacific, and
        # have 2 boolean flags to keep track for each bfs
        # if current point has completed bfs and has 2 flags true, append to res
        pacific, atlantic, res = set(), set(), []
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if r == 0 or c == 0:
                    pacific.add((r, c))
                if r == len(grid) - 1 or c == len(grid[0]) - 1:
                    atlantic.add((r, c))
        
        def bfs(point, res):
            from collections import deque
            q, visited, p_flag, a_flag = deque(), set(), False, False
            q.append(point)
            visited.add(point)

            while q:
                curr = q.popleft()
                if curr in pacific:
                    p_flag = True
                if curr in atlantic:
                    a_flag = True
                
                directions = [[0, 1], [0,-1], [1,0], [-1,0]]
                for d in directions:
                    # boundaries
                    if curr[0] + d[0] < len(grid) and curr[0] + d[0] >= 0 and curr[1] + d[1] < len(grid[0]) and curr[1] + d[1] >= 0 and (curr[0] + d[0], curr[1] + d[1]) not in visited:
                        if grid[curr[0] + d[0]][curr[1] + d[1]] <= grid[curr[0]][curr[1]]:
                            q.append((curr[0] + d[0], curr[1] + d[1]))
                            visited.add((curr[0] + d[0], curr[1] + d[1]))
            if p_flag and a_flag:
                res.append(point)
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                bfs((r, c), res)
        
        return res