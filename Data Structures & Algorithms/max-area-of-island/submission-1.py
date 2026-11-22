class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        Rows, Cols = len(grid),len(grid[0])

        seen = set()
        def dfs(r,c):
            if(r<0 or c<0 or r>=Rows or c>=Cols or grid[r][c] == 0 or (r,c) in seen):
                return 0

            seen.add((r,c))

            area = 1
            for dr, dc in directions:
               area += dfs(r + dr, c + dc)
            
            return area
        
        ans = 0
        for r in range(Rows):
            for c in range(Cols):
                ans = max(ans,dfs(r,c))
        return ans