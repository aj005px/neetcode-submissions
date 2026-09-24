class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #for row checking
        for r in range(9):
            seen = set()
            for i in range(9):
                if board[r][i] == '.':
                    continue
                if board[r][i] in seen:
                    return False
                seen.add(board[r][i])
            
        
        #for column checking

        for c in range(9):
            seen = set()
            for i in range(9):
                if board[i][c] == ".":
                    continue
                if board[i][c] in seen:
                    return False
                seen.add(board[i][c])
        
        #for each square tile
        for s in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (s//3) * 3 + i
                    col = (s % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True
