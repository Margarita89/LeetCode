class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        General idea: Fill boards by row using while loop and a list of boards
        1. Initialize board - list of boards with all options to occupy first row. Store there a tuple of (row, column). 
        2. Use while loop until boards will become empty: all boards will be filled up until last row and will be appended to the list of results
            1. Pop a board from boards
            2. If the size is n - it's already full -> append to res
            3. Iterate through possible values for the column and append to board possible (row, column), where row - is the size of board and is also current row. 
        """
        boards = [[(0, i)] for i in range(n)]
        res = []
        while boards:
            board = boards.pop()
            row = len(board)
            if row == n:
                res.append([
                    ''.join('Q' if i == c else '.' for i in range(n))
                    for r, c in board])
            for column in range(n):
                if all(column != c and abs(column - c) != abs(row - r) for r, c in board):
                    boards.append(board + [(row, column)])
        return res
        