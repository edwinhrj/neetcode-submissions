class Solution:
    def bfs(self, node, visited, rows, cols, grid):
        from collections import deque
        q = deque()
        q.append(node)

        while q:
            curr = q.popleft()
            # define possible 4 direction movement
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for d in directions:
                adj, r, c = (curr[0] + d[0], curr[1] + d[1]), curr[0] + d[0], curr[1] + d[1]
                if r >= 0 and c >= 0 and r < rows and c < cols and grid[r][c] == "1" and adj not in visited:
                    visited.add(adj)
                    q.append(adj)
        
        return visited



    def numIslands(self, grid: List[List[str]]) -> int:
        # for each (r, c) not in visited and if (r, c) is a 1, 
        # we run bfs to add all adjacent 1s to visited
        # increment island by 1
        # return island
        from collections import deque

        visited, q, islands = set(), deque(), 0
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    visited = self.bfs((r, c), visited, rows, cols, grid)
                    islands += 1
        return islands