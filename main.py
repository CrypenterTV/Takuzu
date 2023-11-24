from takuzu import Takuzu
from gridparser import GridParser
import tkinter as tk
from tkinter import font
from main_menu import MainMenu



def main() -> None:
    root = tk.Tk()
    app = MainMenu(root)
    root.mainloop()


if __name__ == "__main__":
    main()

