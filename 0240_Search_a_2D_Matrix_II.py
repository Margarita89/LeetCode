class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        
        1. Start from upper right or lower left corner (our case)
        2. Traverse matrix with while loop on indexes
            - If the value in matrix is larger than target -> move to other row
            - elif the value in matrix is larger than target -> move to other column
            - else: -> return answer
        """
        row, col = len(matrix) - 1, 0
        while row >= 0 and col < len(matrix[0]):
            if matrix[row][col] == target:
                return True
            if matrix[row][col] > target:
                row -= 1
            else:
                col += 1
        return False
        