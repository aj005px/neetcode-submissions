class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        ROWS, COLS = len(heights), len(heights[0])

        p = a = False

        def dfs(r, c, visited):
            nonlocal p, a

            if r < 0 or c < 0:
                p = True
                return

            if r >= ROWS or c >= COLS:
                a = True
                return

            if (r,c) in visited:
                return

            visited.add((r,c))

            for rx,cx in directions:
                nr, nc = r + rx, c + cx

                if 0 <= nr < ROWS and 0 <= nc < COLS:
                    if heights[nr][nc] <= heights[r][c]:
                        dfs(nr, nc, visited)
                else:
                    dfs(nr, nc, visited)

        ans = []

        for r in range(ROWS):
            for c in range(COLS):
                p = a = False
                visited = set()

                dfs(r,c,visited)

                if p and a:
                    ans.append([r,c])

        return ans