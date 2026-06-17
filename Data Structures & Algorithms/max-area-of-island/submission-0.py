from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        rows, cols = len(grid), len(grid[0])
        maxArea = 0

        def bfs(r, c):
            queue = deque()
            grid[r][c] = 0
            queue.append((r, c))
            area = 1
            while queue:
                xr, xc = queue.popleft()
                for dr, dc in directions:
                    nr, nc = dr + xr, dc + xc
                    if (nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] == 0):
                        continue
                    grid[nr][nc] = 0
                    queue.append((nr, nc))
                    area += 1
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, bfs(r, c))

        return maxArea