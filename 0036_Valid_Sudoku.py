class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        General idea: use defaultdict from set for each column, each row and each box to store the values and check up with them. Alternative: traverse 3 times - through columns, rows and boxes and store encountered values in sets and empty sets each time.
        1. Initialize defaultdict from set for each column, each row and each box
        2. Use 2 nested loops to iterate through rows and columns
            1. if value is digit (not '.'):
                1. If value is already in any defaultdict -> return False
                2. Else: add value to all 3 defaultdict by respective key (index from the loop)
        3. Return True
        """
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        boxes = collections.defaultdict(set)
        for i, row in enumerate(board):
            for j, val in enumerate(row):
                if val != '.':
                    if val in cols[j] or val in rows[i] or val in boxes[3*(i//3) + j//3]:
                        return False
                    cols[j].add(val)
                    rows[i].add(val)
                    boxes[3*(i//3) + j//3].add(val)
        return True 
                    s