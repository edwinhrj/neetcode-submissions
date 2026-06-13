class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # for each node, run a bfs
        # multi source bfs from treasure chest
        # add all treasure points to a queue
        # run bfs on grid, only modifying the grid per "level" the grid
        from collections import deque
        q, visited, dist, m, n = deque(), set(), 1, len(grid) - 1, len(grid[0]) - 1
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))
        
        while q:
            for i in range(len(q)):
                curr = q.popleft()
                r, c = curr[0], curr[1]
                directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
                for d in directions:
                    nr, nc = r + d[0], c + d[1]
                    if nr <= m and nr >= 0 and nc <= n and nc >= 0:
                        if (nr, nc) not in visited and grid[nr][nc] != -1:
                            grid[nr][nc] = dist
                            q.append((nr, nc))
                            visited.add((nr, nc))
            dist += 1
        

        

    


                        


