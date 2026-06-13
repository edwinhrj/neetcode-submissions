class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # level bfs
        # multi source bfs from rotten fruit
        # init time
        # add all grid[2] to q, init fresh; for each level pop all and check
        # for adjacent points, if got fresh; fresh ++
        # if move on to next level and fresh == 0 still, return -1 else continue
        from collections import deque

        q, visited, total_fresh, time = deque(), set(), 0, 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    q.append((r, c))
                    visited.add((r, c))
                
                if grid[r][c] == 1:
                    total_fresh += 1
        
        # multi source bfs
        while q and total_fresh > 0:
            time += 1
            for _ in range(len(q)):
                curr = q.popleft()
                r, c = curr[0], curr[1]
                directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
                for d in directions:
                    nr, nc = r + d[0], c + d[1]
                    if (nr, nc) not in visited and nr <= len(grid) -1 and nr >= 0 and nc <= len(grid[0]) - 1 and nc >= 0:
                        if grid[nr][nc] == 1:
                            total_fresh -= 1
                            visited.add((nr, nc))
                            q.append((nr, nc))
        
        return time if total_fresh == 0 else -1

