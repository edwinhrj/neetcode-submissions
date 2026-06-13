class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # for each node, run a bfs
        # multi source bfs from treasure chest

        def bfs(point, grid, m, n):
            from collections import deque
            q, visited, dist = deque(), set(), 0
            q.append(point)
            visited.add(point)

            while q:
                dist += 1 
                for i in range(len(q)): # process all nodes in same lvl before updating dist
                    curr_point = q.popleft()
                    r, c = curr_point[0], curr_point[1]
                    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                    for d in directions:
                        nr, nc = r + d[0], c + d[1]
                        new_point = (nr, nc)
                        # check boundaries
                        if r + d[0] <= m and r + d[0] >= 0 and c + d[1] <= n and c + d[1] >= 0:
                            if new_point not in visited and grid[nr][nc] != -1:
                                # if new point has already been marked by a previous bfs,
                                # take the shorter distance
                                if grid[nr][nc] > dist:
                                    grid[nr][nc] = dist
                                q.append(new_point)
                                visited.add(new_point)
        
        m, n = len(grid) - 1, len(grid[0]) - 1
        for r in range(m + 1):
            for c in range(n + 1):
                if grid[r][c] == 0:
                    # call bfs
                    bfs((r, c), grid, m, n)
    


                        


