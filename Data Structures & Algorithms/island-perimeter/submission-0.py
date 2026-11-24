class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        direction = [[1,0], [-1,0], [0,1], [0,-1]]
        ROWS, COLS = len(grid), len(grid[0])

        seen = set()

        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return 1

            if grid[r][c] == 0:
                return 1

            if (r, c) in seen:
                return 0

            seen.add((r, c))

            count = 0

            for dr, dc in direction:
                count += dfs(r + dr, c + dc)

            return count

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return dfs(r, c)

        return 0