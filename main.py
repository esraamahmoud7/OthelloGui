import tkinter as tk
from Controller import OthelloGame

root = tk.Tk()
othello_game = OthelloGame(master=root)
othello_game.mainloop()

