from takuzu import Takuzu, generate_takuzu
from gridparser import GridParser
import tkinter as tk
from tkinter import font
from main_menu import MainMenu
from takuzu_menu import TakuzuMenu



def main() -> None:

    root = tk.Tk()
    app = MainMenu(root)
    root.mainloop()



if __name__ == "__main__":
    main()

