# from OthelloState import OthelloGameState


# State Representation
# OthelloBoard.py


class DummyBoard:
    def __init__(self, board=None):
        if board is None:
            board = [['_' for j in range(8)] for i in range(8)]
        self.board = board

    def __getitem__(self, key):
        return self.board[key]

    def has_empty_places(self):
        for row in self.board:
            if '_' in row:
                return True
        return False

    def print_board(self, current_player):
        print("Current Player:", current_player)
        print("   0 1 2 3 4 5 6 7")
        print("  -----------------")
        for i, row in enumerate(self.board):
            print(str(i) + "|", ' '.join(row))
        print("\n")

    # (1, 0): Downward in same column.
    # (-1, 0): Upward in same column.
    # (0, 1): Rightward ins ame row.
    # (0, -1): Leftward in same row.
    # (1, 1): Diagonal down-right
    # (-1, -1): Diagonal up-left
    # (1, -1): Diagonal down-left
    # (-1, 1): Diagonal up-right

    # Update Board after each move
    def update_Board(self, row, col, current_player):
        self.board[row][col] = current_player
        AvailDir = [(0, 1), (1, 0), (0, -1), (-1, 0)] #(1, 1), (-1, -1), (1, -1), (-1, 1)
        for dr, dc in AvailDir:
            flip = []
            r, c = row + dr, col + dc
            while 0 <= r < 8 and 0 <= c < 8 and self.board[r][c] != '_' and self.board[r][c] != current_player:
                flip.append((r, c))
                # still move in same direction untill we find our own piece or reach to boundry
                r += dr
                c += dc
            # checks if the indices r and c are within the bounds of the board
            # reach to disk of current player so start flip the disk
            if 0 <= r < 8 and 0 <= c < 8 and self.board[r][c] == current_player:
                for r, c in flip:
                    self.board[r][c] = current_player

    def update_Board_Computer(self,Board,row, col, current_player):
        Board[row][col] = current_player
        AvailDir = [(0, 1), (1, 0), (0, -1), (-1, 0)] #(1, 1), (-1, -1), (1, -1), (-1, 1)
        for dr, dc in AvailDir:
            flip = []
            r, c = row + dr, col + dc
            while 0 <= r < 8 and 0 <= c < 8 and Board[r][c] != '_' and Board[r][c] != current_player:
                flip.append((r, c))
                # still move in same direction untill we find our own piece or reach to boundry
                r += dr
                c += dc
            # checks if the indices r and c are within the bounds of the board
            # reach to disk of current player so start flip the disk
            if 0 <= r < 8 and 0 <= c < 8 and Board[r][c] == current_player:
                for r, c in flip:
                    Board[r][c] = current_player
        return Board
