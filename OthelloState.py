

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

    def Possible_Moves_User(self,board):
        valid_Moves = []
        # Check all possible moves
        for row in range(8):
            for col in range(8):
                if board[row][col] == '_':
                    # Check if the move is valid
                    if self.is_valid_move_User(row, col,board):
                        valid_Moves.append((row, col))
        return valid_Moves

    def is_valid_move_User(self, row, col,board):
        flag = False
        AvailDir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dr, dc in AvailDir:
            r, c = row + dr, col + dc
            while 0 <= r < 8 and 0 <= c < 8 and board[r][c] != '_' and board[r][c] != 'B':
                r, c = r + dr, c + dc
                flag = True

            if flag and 0 <= r < 8 and 0 <= c < 8 and board[r][c] == 'B':
                return True
            flag = False

        return False
    def update_Board_Computer(self, Board, row, col, current_player):
        Board[row][col] = current_player
        AvailDir = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # (1, 1), (-1, -1), (1, -1), (-1, 1)
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

    def alpha_beta_Purned(self, first, testBoard, depth, alpha, beta, ComputerTurn):
        # if depth = 0 or no more moves can be made for 2 players (Game over) return the utility function
        if depth == 0 or (self.Possible_Moves_Computer(testBoard) == [] and self.Possible_Moves_User(testBoard) == []):
            # when arrive to leaf you need to call utility Function and return None for move can't make
            return self.Utility(testBoard), None
        print("Depth: ", depth)
        if ComputerTurn:
            if first:
                first = False
                print("Computer Turn")
                print("   0 1 2 3 4 5 6 7")
                print("  -----------------")
                for i, row in enumerate(testBoard.board):
                    print(str(i) + "|", ' '.join(row))
            # if computer play gave a list for all valid moves can machine make
            validMoves = self.Possible_Moves_Computer(testBoard)
            if validMoves == []:
                evaluate, _ = self.alpha_beta_Purned(False, testBoard, depth - 1, alpha, beta, False)
            print(validMoves)
            # init maxVal with negative value at first to start evaluate valid moves
            maxVal = -10000
            bestMove = None  # at first time best move is none
            for move in validMoves:
                # ------------------------------------------
                # make a deep cop for board to test alpha
                TestedBoard=[row[:] for row in testBoard]
                TestedBoard = self.update_Board_Computer(TestedBoard, move[0], move[1], 'W')

                # player turn
                evaluate, _ = self.alpha_beta_Purned(False, TestedBoard, depth - 1, alpha, beta, False)
                if evaluate > maxVal:  # if evaluate val is bigger than maxVal so make maxVal = eval alpha take max
                    maxVal = evaluate
                    bestMove = move
                    alpha = max(alpha, evaluate)
                    if alpha >= beta:
                        break  # when alpha is bigger than betta stop this branch don't continue
            return maxVal, bestMove  # return max and the move
        else:  # every thing we make in alpha do with beta but with min not max
            validMovs = self.Possible_Moves_User(testBoard)
            if validMovs == []:
                evaluate, _ = self.alpha_beta_Purned(False, testBoard, depth - 1, alpha, beta, True)
            minVal = 10000
            bestMove = None
            for move in validMovs:
                TestedBoard =[row[:] for row in testBoard]
                TestedBoard = self.update_Board_Computer(TestedBoard, move[0], move[1], 'B')
                evaluate, _ = self.alpha_beta_Purned(False, TestedBoard, depth - 1, alpha, beta, True)
                if evaluate < minVal:
                    minVal = evaluate
                    bestMove = move
                    beta = min(beta, evaluate)
                    if beta <= alpha:
                        break
            return minVal, bestMove

    def Utility(self, testBoard):
        black_Score = 0
        white_Score = 0
        for row in testBoard:
            for cell in row:
                if cell == 'B':
                    black_Score += 1
                elif cell == 'W':
                    white_Score += 1
        return white_Score - black_Score

    def Possible_Moves_Computer(self, TestBoard):
        valid_Moves = []
        # Check all possible moves
        for row in range(8):
            for col in range(8):
                if TestBoard[row][col] == '_':  ## problem in thisss
                    # Check if the move is valid
                    if self.is_valid_move_Computer(row, col, TestBoard):
                        valid_Moves.append((row, col))
        return valid_Moves  # Corrected indentation

    def is_valid_move_Computer(self, row, col, TestBoard):
        flag = False
        AvailDir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dr, dc in AvailDir:
            r, c = row + dr, col + dc
            while 0 <= r < 8 and 0 <= c < 8 and TestBoard[r][c] != '_' and TestBoard[r][c] != 'W':
                r, c = r + dr, c + dc
                flag = True

                if flag and 0 <= r < 8 and 0 <= c < 8 and TestBoard[r][c] == 'W':
                    return True

                flag = False

        return False

    ##Not implemented
    # def make_move(self, row, col):
    #     pass

    ##Not implemented
    # def is_valid_move(self, row, col):
    #     # Check if the move is within bounds and the cell is empty
    #     return 0 <= row < self.board.size and 0 <= col < self.board.size and self.board.board[row][col] == ' '
