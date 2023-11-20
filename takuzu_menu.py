import tkinter as tk
from tkinter import ttk, font
from takuzu import Takuzu
from gridparser import GridParser


locations = []

def create_label_grid(grid, parent, solved=False):
    custom_font = font.nametofont("TkDefaultFont")
    custom_font.configure(size=20)

    for i in range(len(grid)):
        for j in range(len(grid)):
            text = grid[i][j]
            if text == -1:
                text = '_'
                locations.append((i,j))
            if solved:
                if (i, j) in locations:
                    label = tk.Label(parent, text=f"{text}", width=4, height=2, borderwidth=1, relief="solid", font=custom_font, fg='red')
                    label.grid(row=i, column=j)
                else:
                    label = tk.Label(parent, text=f"{text}", width=4, height=2, borderwidth=1, relief="solid", font=custom_font)
                    label.grid(row=i, column=j)
            else:  
                label = tk.Label(parent, text=f"{text}", width=4, height=2, borderwidth=1, relief="solid", font=custom_font)
                label.grid(row=i, column=j)



class TakuzuMenu:

    def __init__(self, root : tk.Tk, takuzu : Takuzu, takuzu_solved : Takuzu):
        root.title("Takuzu")

        table = tk.Frame(root)
        table.grid(row=0, column=0)

        custom_font = font.nametofont("TkDefaultFont")
        custom_font.configure(size=20)


        unsolved_label_frame = tk.LabelFrame(table, text="Unsolved Grid")
        unsolved_label_frame.grid(row=0, column=0)
        create_label_grid(takuzu.get_grid(), unsolved_label_frame)

        # Create labels for the solved grid
        solved_label_frame = tk.LabelFrame(table, text="Solved Grid")
        solved_label_frame.grid(row=0, column=1)
        create_label_grid(takuzu_solved.get_grid(), solved_label_frame, solved=True)

