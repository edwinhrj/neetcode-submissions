class Solution:
    def solve(self, grid: List[List[str]]) -> None:
        # first find surrounded regions
        # modify them in place

        # multi source bfs from the edge points, process all 'o's
        # go through every point in grid, if point not in visited and is 'o', conevrt to 'X'

        from collections import deque
        q = deque()
        visited = set()
        # add all edge points into q 
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if r == 0 or r == len(grid) - 1:
                    if grid[r][c] == 'O':
                        visited.add((r,c))
                        q.append((r,c))
                if c == 0 or c == len(grid[0]) - 1:
                    if grid[r][c] == 'O':
                        visited.add((r,c))
                        q.append((r,c))
        
        while q:
            curr = q.popleft()
            directions = [[0,1], [0,-1], [1,0], [-1,0]]
            for d in directions:
                nr, nc = curr[0] + d[0], curr[1] + d[1]
                if nr <= len(grid) - 1 and nr >= 0 and nc <= len(grid[0]) - 1 and nc >= 0:
                    if grid[nr][nc] == 'O' and (nr, nc) not in visited:
                        q.append((nr, nc))
                        visited.add((nr, nc))
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r, c) not in visited and grid[r][c] == 'O':
                    grid[r][c] = 'X'

        

