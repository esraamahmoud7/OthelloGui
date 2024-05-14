import tkinter as tk
from random import choice

from DummyBoard import DummyBoard
from OthelloBoard import OthelloBoard
from OthelloState import OthelloGameState


class OthelloGame(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.board_gui = OthelloBoard(self,master=self)
        self.GameState = OthelloGameState(self.board_gui)
        self.create_widgets()

    def SwitchPlayer(self, row, col):
        self.GameState.switch_player()
        BScore,WScore =self.GameState.Calculate_Score()
        self.board_gui.update_score_labels(BScore,WScore)

        if self.GameState.human_turn:
            self.handle_human_move(row, col)

        else:
            self.board_gui.remove_valid_effects()
            self.handle_computer_move()

    def create_widgets(self):
        # Create a label to display current player
        self.current_player_label = tk.Label(self, text="Current Player: " + self.GameState.current_player,
                                             font=("Helvetica", 12))
        self.current_player_label.pack()

        # Create a button to start a new game
        # self.new_game_button = tk.Button(self, text="New Game", command=self.start_new_game)
        # self.new_game_button.pack()

        # Create a button to quit the game
        self.quit_button = tk.Button(self, text="Quit", command=self.quit_game)
        self.quit_button.pack()

    def update_current_player_label(self):
        # Update the text of the current player label
        self.current_player_label.config(text="Current Player: " + self.GameState.current_player)

    def start_new_game(self):
        # Reset the game state (clear the board, set current player, etc.)
        self.board_gui.reset_board()
        self.current_player_label.config(text="Current Player: Black")  # Start with Black player

    def quit_game(self):
        # Logic to quit the game goes here
        self.quit()

    def handle_human_move(self, row, col):

        valid_Moves = self.GameState.Possible_Moves_User()
        self.board_gui.update_buttons(valid_Moves)
        # if self.board_gui.board[row][col] != 'B' and self.board_gui.board[row][col] != 'W':
        #     print("Invalid move")
        #     return
        # while (row,col) not in valid_Moves:
        #     print("Invalid move")

        self.board_gui.on_click(row, col, self.GameState.current_player)
        self.GameState.Calculate_Score()
        self.GameState.switch_player()
        self.update_current_player_label()

    def handle_computer_move(self):
        #Get possible moves
        # empty_cells = [(i, j) for i in range(8) for j in range(8) if self.board_gui.board[i][j] == '_']
        # if empty_cells:
        #     valid_moves = []

            # for row, col in valid_Moves:
            #     if self.is_valid_move(row, col):
            #         valid_moves.append((row, col))
            testBoard = OthelloBoard(self)
            testBoard.board = [row[:] for row in self.board_gui.board]
            dummyBoard = DummyBoard(testBoard.board)
             # return tuple from alpha beta
            best_move = self.GameState.alpha_beta_Purned(True, dummyBoard, 3, -1000, 1000, True)
            print(best_move)
            self.board_gui.on_click(best_move[1][0], best_move[1][1], self.GameState.current_player)
            self.GameState.Calculate_Score()
            self.GameState.switch_player()

    def is_valid_move(self, row, col):
        if self.board_gui.board[row][col] != '_':
            return False
        else:
            return True

        # def SwitchPlayer(self, row, col):
            #     if self.GameState.human_turn:
            #         if self.board_gui.board[row][col] != 'B' and self.board_gui.board[row][col] != 'W':
            #             #get valid move
            #             self.board_gui.update_Board(row, col, self.GameState.current_player)
            #             #self.board_gui.print_Board(self.GameState.current_player)
            #             self.GameState.Calculate_Score()
            #             self.GameState.switch_player()
            #
            #         else:
            #             print("Invalid move")
            #     else:
            #         empty_cells = [(i, j) for i in range(8) for j in range(8) if self.board_gui.board[i][j] != 'B' and self.board_gui.board[i][j] != 'W']
            #         if empty_cells:
            #             row, col = choice(empty_cells)
            #             self.board_gui.update_Board(row, col, self.GameState.current_player)
            #             #self.board_gui.print_Board(self.GameState.current_player)
            #             self.GameState.Calculate_Score()
            #             self.GameState.switch_player()
