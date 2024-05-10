
# from OthelloBoard import OthelloBoard


class OthelloGameState:
    def __init__(self, Board):
        self.current_player = 'B'
        self.board = Board
        self.human_turn = True

    def switch_player(self):
        if self.current_player == 'B':
            self.current_player = 'W'
            self.human_turn = False
        else:
            self.current_player = 'B'
            self.human_turn = True

    def Calculate_Score(self):
        black_Score = 0
        white_Score = 0
        for row in self.board.board:
            for cell in row:
                if cell == 'B':
                    black_Score += 1
                elif cell == 'W':
                    white_Score += 1
        return black_Score, white_Score


    ##Not implemented
    # def make_move(self, row, col):
    #     pass

    ##Not implemented
    # def is_valid_move(self, row, col):
    #     # Check if the move is within bounds and the cell is empty
    #     return 0 <= row < self.board.size and 0 <= col < self.board.size and self.board.board[row][col] == ' '
