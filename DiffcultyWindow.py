import tkinter as tk


class DifficultyWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.diffculty = 0
        self.title("Choose Difficulty")
        self.geometry("450x450")
        # self.controller = controller

        self.label = tk.Label(self, text="\n \n \n \n \n \n \n \nSelect Difficulty:",font=("Helvetica", 12))
        self.label.pack()

        self.easy_button = tk.Button(self, text="Easy", command=self.set_easy, width=10, bg="#0A5C36", fg="white",font=("Helvetica", 12))
        self.easy_button.pack(pady=10)

        self.medium_button = tk.Button(self, text="Medium", command=self.set_medium, width=10, bg="#14452F", fg="white",font=("Helvetica", 12))
        self.medium_button.pack(pady=10)

        self.hard_button = tk.Button(self, text="Hard", command=self.set_hard, width=10, bg="#18392B", fg="white",font=("Helvetica", 12))
        self.hard_button.pack(pady=10)

    def set_easy(self):
        self.diffculty=1
        self.destroy()
        # self.controller.show_board()  # Show the board window

    def set_medium(self):
        self.diffculty=2
        self.destroy()  # Close the difficulty window
        # self.controller.show_board()  # Show the board window

    def set_hard(self):
        self.diffculty=3
        self.destroy()  # Close the difficulty window
        # self.controller.show_board()  # Show the board window