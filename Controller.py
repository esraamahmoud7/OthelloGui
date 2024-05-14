import tkinter as tk

from OthelloBoard import OthelloBoard
from OthelloState import OthelloGameState


class OthelloGame(tk.Frame):

    def __init__(self, master=None,level=None):
        super().__init__(master)
        self.level=level
        print(self.level)
        self.pack()
        self.count = 0
        self.BlackDisks,self.WhiteDisks = 30,30
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
            self.handle_computer_move(row,col)

    def create_widgets(self):
        # Create a label to display current player
        self.current_player_label = tk.Label(self,
                                             font=("Helvetica", 12))
        self.current_player_label.pack()

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
        if self.WhiteDisks == 0 or self.BlackDisks == 0:
            self.winner("End")
            return

        valid_Moves = self.GameState.Possible_Moves_User()

        if not valid_Moves and self.board_gui.has_white_nodes() and self.count == 0:

            self.count += 1
            self.SwitchPlayer(row, col)
            return
        # when no available move for both player and computer
        elif self.count > 0:
            self.winner("No Moves")
            return
        self.board_gui.update_buttons(valid_Moves)
        self.board_gui.on_click(row, col, self.GameState.current_player)
        self.GameState.Calculate_Score()
        self.GameState.switch_player()
        self.count = 0
        self.BlackDisks -= 1
        self.update_current_player_label()

    def handle_computer_move(self,row,col):
        if not self.GameState.Possible_Moves_Computer(self.board_gui) and self.board_gui.has_black_nodes() and self.count == 0:
            self.count += 1
            self.SwitchPlayer(row,col)
            return

        testBoard = OthelloBoard(self)
        testBoard.board = [ro[:] for ro in self.board_gui.board]

        if self.level == 1:
            best_move = self.GameState.alpha_beta_Purned(True, testBoard,1, -1000, 1000, True)

        elif self.level == 2:
            best_move = self.GameState.alpha_beta_Purned(True, testBoard, 2, -1000, 1000, True)

        elif self.level == 3:
            best_move = self.GameState.alpha_beta_Purned(True, testBoard, 3, -1000, 1000, True)

        if best_move[0] == -10000 or best_move[0] == 10000:
            self.count += 1
            self.SwitchPlayer(row, col)
            return

        # return tuple from alpha beta
        print(best_move)
        self.board_gui.on_click(best_move[1][0], best_move[1][1], self.GameState.current_player)
        self.GameState.Calculate_Score()
        self.GameState.switch_player()
        self.count = 0
        self.WhiteDisks -= 1

    def is_valid_move(self, row, col):
        if self.board_gui.board[row][col] != '_':
            return False
        else:
            return True


    def winner(self,state):
        BScore, WScore = self.GameState.Calculate_Score()
        # self.board_gui.destroy()
        # self.current_player_label.destroy()

        # Destroy the quit button
        # self.quit_button.destroy()
        winner_window = tk.Toplevel(self)
        winner_window.title(state)
        winner_window.geometry("300x200")

        winner_label = tk.Label(winner_window, text="End!\n\n")
        winner_label.pack()

        if BScore > WScore:
            winner_label.config(text="Player wins!")
        elif WScore > BScore:
            winner_label.config(text="AI wins!")
        else:
            winner_label.config(text="It's a draw!")

        # Add a button to close the winner window
        close_button = tk.Button(winner_window, text="Close", command=winner_window.destroy)
        close_button.pack()

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
