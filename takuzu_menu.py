import tkinter as tk
from tkinter import ttk, font
from takuzu import Takuzu
from gridparser import GridParser
import main_menu

def create_label_grid(grid, parent):
    custom_font = font.nametofont("TkDefaultFont")
    custom_font.configure(size=20)

    for i in range(len(grid)):
        for j in range(len(grid)):
            text = grid[i][j]
            if text == -1:
                text = '_'
            label = tk.Label(parent, text=f"{text}", width=4, height=2, borderwidth=1, relief="solid", font=custom_font)
            label.grid(row=i, column=j)



class TakuzuMenu:

    def __init__(self, root : tk.Tk, takuzu : Takuzu, takuzu_solved : Takuzu):

        self.root = root

        self.root.title("Jeu du Takuzu")

        #main_menu.center_window(self.root)
        self.root.resizable(False, False)
        table = tk.Frame(self.root)
        table.grid(row=0, column=0)

        custom_font = font.nametofont("TkDefaultFont")
        custom_font.configure(size=20)


        unsolved_label_frame = tk.LabelFrame(table, text="Grille de départ")
        unsolved_label_frame.grid(row=0, column=0)
        create_label_grid(takuzu.get_grid(), unsolved_label_frame)


        #solved_label_frame = tk.LabelFrame(table, text="Grille Résolue")
        #solved_label_frame.grid(row=0, column=1)
        #create_label_grid(takuzu_solved.get_grid(), solved_label_frame)

        root.update_idletasks()
        main_menu.center_window(root, root.winfo_width(), root.winfo_height(), 25)
        

