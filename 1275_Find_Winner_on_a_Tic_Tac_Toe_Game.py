class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        """
        General idea: create a set of game_A and game_B for lookup in O(1)
        1. Create sets game_A and game_B with tuples from moves
        2. Method to check if the game was won by the player:
            1. Check columns and rows
            2. Check diagonal and anti-diagonal
        3. Check of player A and B
        4. Check if the game is over (in that case there is no winner)
        5. Lase case -> 'Pending'
        """
        
        game_A = {tuple(move) for i, move in enumerate(moves) if i % 2 == 0}
        game_B = {tuple(move) for i, move in enumerate(moves) if i % 2 == 1}
        
        def check_player(game):
            diag, anti_diag = 0, 0
            for i in range(3):
                count_col, count_row = 0, 0
                for j in range(3):
                    if (j, i) in game:
                        count_row += 1
                    if (i, j) in game:
                        count_col += 1
                if count_row == 3 or count_col == 3:
                    return True
                if (i, i) in game:
                    diag += 1
                if (2 - i, i) in game:
                    anti_diag += 1
            return diag == 3 or anti_diag == 3
        
        if check_player(game_A):
            return "A"
        if check_player(game_B):
            return "B"
        
        if len(moves) == 9:
            return "Draw"
        return "Pending"