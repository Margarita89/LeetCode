class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        General idea: rotate upper left corner
        1. Use 2 nested loops to iterate through upper left corner. Attention to even and odd values of matrix size
        2. Change all for cells in place
        """
        n = len(matrix)
        for i in range(n // 2):
            for j in range((n + 1) // 2):
                matrix[i][j], matrix[j][~i], matrix[~i][~j], matrix[~j][i] = matrix[~j][i], matrix[i][j], matrix[j][~i], matrix[~i][~j]
