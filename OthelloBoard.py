import tkinter as tk

class OthelloBoard(tk.Frame):
    def __init__(self, controller, master=None):
        super().__init__(master)
        self.pack()
        self.board = [['_' for _ in range(8)] for _ in range(8)]
        self.board[3][3] = 'W'
        self.board[3][4] = 'B'
        self.board[4][3] = 'B'
        self.board[4][4] = 'W'
        self.controller = controller
        self.black_score_label = '2'
        self.white_score_label = '2'
        self.draw_board()

    def draw_board(self):
        cell_size = 50
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == 'W' or self.board[i][j] == 'B':
                    state = 'disabled'  # Disable the button if the cell is not empty
                else:
                    state = 'normal'  # Enable the button for empty cells
                button = tk.Button(self, width=6, height=3, bd=1, relief="solid", bg="dark green",
                                   command=lambda row=i, col=j: self.on_click(row, col,'B'), state=state)
                button.grid(row=i, column=j)
                self.create_score_labels()
                self.update_cell(i, j)

    def create_score_labels(self):
        # Create labels to display scores
        self.black_score_label = tk.Label(self, text="Black: 2",font=("Helvetica", 12))
        self.white_score_label = tk.Label(self, text="White: 2",font=("Helvetica", 12))
        self.black_score_label.grid(row=8, column=0, columnspan=4)
        self.white_score_label.grid(row=8, column=4, columnspan=4)

    def update_score_labels(self, black_score, white_score):
        self.black_score_label.config(text=f"Black: {black_score}",font=("Helvetica", 12))
        self.white_score_label.config(text=f"White: {white_score}",font=("Helvetica", 12))

    def update_cell(self, row, col):
        if self.board[row][col] == 'B':
            color = "black"
        elif self.board[row][col] == 'W':
            color = "white"
        else:
            color = "dark green"
        self.grid_slaves(row=row, column=col)[0].config(bg=color)

    def update_Board(self, row, col, current_player):
        if self.board[row][col] != '_':
            return False
        self.board[row][col] = current_player
        AvailDir = [(0, 1), (1, 0), (0, -1), (-1, 0)]  #(1, 1), (-1, -1), (1, -1), (-1, 1)
        for dr, dc in AvailDir:
            disks = []
            r, c = row + dr, col + dc
            while 0 <= r < 8 and 0 <= c < 8 and self.board[r][c] != '_' and self.board[r][c] != current_player:
                disks.append((r, c))
                r += dr
                c += dc
            if 0 <= r < 8 and 0 <= c < 8 and self.board[r][c] == current_player:
                for fr, fc in disks:
                    self.board[fr][fc] = current_player
                    self.update_cell(fr, fc)

    def on_click(self, row, col,current_player):
         # Assuming black player starts
        if self.board[row][col] == '_':
            self.update_Board(row, col, current_player)
            self.update_cell(row, col)
            self.controller.SwitchPlayer(row, col)  # Call SwitchPlayer in the controller

    # def reset_board(self):
    #     self.board = [['_' for _ in range(8)] for _ in range(8)]
    #     self.board[3][3] = 'W'
    #     self.board[3][4] = 'B'
    #     self.board[4][3] = 'B'
    #     self.board[4][4] = 'W'
    #     for i in range(8):
    #         for j in range(8):
    #             self.update_cell(i, j)



# def get_valid_moves(self):
    #     valid_moves=[]
    #     for row in range(8):
    #         for col in range(8):
    #             if self.board[row][col] == ' ' and self.is_valid_move(row, col):
    #                 valid_moves.append((row, col))
    #     return valid_moves
    # (row,column).
    # (1, 0): Downward in same column.
    # (-1, 0): Upward in same column.
    # (0, 1): Rightward ins ame row.
    # (0, -1): Leftward in same row.
    # (1, 1): Diagonal down-right
    # (-1, -1): Diagonal up-left
    # (1, -1): Diagonal down-left
    # (-1, 1): Diagonal up-righ
    # def is_valid_move(self, row, col):
    #     directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    #     for validR, validC in directions:
    #         r, c = row + validR, col + validC
    #         #in board boundry
    #         if not (0 <= r < 8 and 0 <= c < 8):
    #             continue
    #             ##??????