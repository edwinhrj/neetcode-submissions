class Solution:
    def bfs(self, node, visited, row, col, grid, area):
        from collections import deque
        q = deque()
        q.append(node)
        visited.add(node)

        while q:
            curr = q.popleft()
            # define directional movement
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for d in directions:
                adj, r, c = (curr[0] + d[0], curr[1] + d[1]), curr[0] + d[0], curr[1] + d[1]
                if r >= 0 and c >= 0 and r < row and c < col and grid[r][c] == 1 and adj not in visited:
                    area += 1
                    visited.add(adj)
                    q.append(adj)
        return visited, area



    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # init max_area
        # for each node, if node == 1 and not in visited, call bfs to visit all adj nodes == 1 and sum area
        # and add into visited

        # update max_area
        row, col, visited, max_area = len(grid), len(grid[0]), set(), 0

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1 and (r, c) not in visited:
                    area = 1
                    visited, area = self.bfs((r, c), visited, row, col, grid, area)
                    max_area = max(area, max_area)
        
        return max_area
