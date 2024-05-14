import tkinter as tk
from Controller import OthelloGame
from DiffcultyWindow import DifficultyWindow


def start_game(difficulty):
    # root.destroy()  # Close the difficulty window
    othello_game = OthelloGame(master=root, level=difficulty)
    othello_game.mainloop()


root = tk.Tk()

level = DifficultyWindow(parent=root)

# Wait for user interaction to set the difficulty
root.wait_window(level)
diff = level.diffculty

if diff != 0:  # Check if a difficulty level was selected
    start_game(diff)
