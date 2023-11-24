import tkinter as tk
from tkinter import ttk, filedialog
from takuzu_menu import TakuzuMenu
from gridparser import GridParser
import os


#Vert
MENU_BACKGROUND = "#41B77F"

def center_window(root : tk.Tk, window_width, window_height, percentage=10) -> None:
        screen_width, screen_height = root.winfo_screenwidth(), root.winfo_screenheight()

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2 - round(percentage/100 * (screen_height - window_height))

        root.geometry(f"{window_width}x{window_height}+{x}+{y}")


class MainMenu:

    def __init__(self, root : tk.Tk) -> None:

        self.root = root
        self.root.title("Jeu du Takuzu")

        window_width, window_height  = 500, 350
        center_window(root, window_width, window_height)

        self.root.resizable(False, False)

        self.root.config(background=MENU_BACKGROUND)

        style = ttk.Style()
        style.configure("TButton", padding=6, relief="flat", background="#ccc")
        
        title_label = tk.Label(root, text="Jeu du Takuzu", font=("Courrier", 30, 'bold'), bg=MENU_BACKGROUND, fg="white")
        title_label.pack(pady=20)


        random_button = tk.Button(root, text="Résoudre une grille aléatoire", font=("Courrier", 15, 'bold'), bg="white", fg="black", command=print)
        random_button.pack(pady=10)

        file_button = tk.Button(root, text="Charger une grille depuis un fichier", font=("Courrier", 15, 'bold'), bg="white", fg="black", command=self.load_from_file)
        file_button.pack(pady=10)

        quit_button = tk.Button(root, text="Quitter le programme", font=("Courrier", 15, 'bold'), bg="white", fg="red", command=exit)
        quit_button.pack(pady=10)

    def load_from_file(self) -> None:

        file_path = self.choose_file()

        if file_path:
            
            self.root.destroy()
            r = tk.Tk()
            parser = GridParser(file_path)
            takuzu = parser.get_takuzu()
            assert takuzu != None
            print(takuzu)
            tk_menu = TakuzuMenu(r, takuzu, file_path.split('/')[-1])
            
        

    def choose_file(self):
        file_path = filedialog.askopenfilename(title="Sélectionner un fichier", filetypes=[("Fichiers texte", "*.txt")])

        return file_path
    
    def get_root(self):
        return self.root

    






