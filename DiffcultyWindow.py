import tkinter as tk


class DifficultyWindow(tk.Toplevel):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.diffculty=0
        self.title("Choose Difficulty")
        self.geometry("500x500")
        self.controller = controller

        self.label = tk.Label(self, text="Select Difficulty:")
        self.label.pack()

        self.easy_button = tk.Button(self, text="Easy", command=self.set_easy)
        self.easy_button.pack()

        self.medium_button = tk.Button(self, text="Medium", command=self.set_medium)
        self.medium_button.pack()

        self.hard_button = tk.Button(self, text="Hard", command=self.set_hard)
        self.hard_button.pack()

    def set_easy(self):
        self.diffculty=1
        self.destroy()  # Close the difficulty window
        self.controller.show_board()  # Show the board window

    def set_medium(self):
        self.diffculty=2
        self.destroy()  # Close the difficulty window
        self.controller.show_board()  # Show the board window

    def set_hard(self):
        self.diffculty=3
        self.destroy()  # Close the difficulty window
        self.controller.show_board()  # Show the board window