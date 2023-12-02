import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from takuzu_menu import TakuzuMenu
from gridparser import GridParser
from random import randint
from takuzu import generate_takuzu


# Paramètres principaux et globaux du menu

MENU_BACKGROUND = "#41B77F" # Couleur d'arrière plan des menus. (vert)
SIZE_MENU = False
DIFFICULTY_MENU = False

# Fonction permettant de centrer une fenêtre (avec un léger décalage vers le haut).
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


        random_button = tk.Button(root, text="Résoudre une grille aléatoire", font=("Courrier", 15, 'bold'), bg="white", fg="black", command=self.random_grid_selection)
        random_button.pack(pady=10)

        file_button = tk.Button(root, text="Charger une grille depuis un fichier", font=("Courrier", 15, 'bold'), bg="white", fg="black", command=self.load_from_file)
        file_button.pack(pady=10)

        quit_button = tk.Button(root, text="Quitter le programme", font=("Courrier", 15, 'bold'), bg="white", fg="red", command=exit)
        quit_button.pack(pady=10)

    def load_from_file(self) -> None:

        file_path = self.choose_file()

        if file_path:
            
            parser = GridParser(file_path)
            takuzu = parser.get_takuzu()
            if takuzu == None:
                messagebox.showerror("Erreur", f"Le fichier {file_path} ne contient pas une grille de takuzu valide.")
                return
            print(takuzu)
            self.root.destroy()
            r = tk.Tk()
            tk_menu = TakuzuMenu(r, takuzu, file_path.split('/')[-1])
    

    def choose_size_parameter(self, size : int, submenu : tk.Toplevel) -> None:
        self.on_closing_size_menu(submenu)
        self.difficulty_menu(size)

    def choose_diff_parameter(self, difficulty : str, submenu : tk.Toplevel, size_str : str) -> None:

        self.on_closing_diff_menu(submenu)

        size = 4

        if size_str.__contains__("6x6"):
            size = 6
        elif size_str.__contains__("8x8"):
            size = 8
        elif size_str.__contains__("10x10"):
            size = 10
        
        rate = 100

        if difficulty.__contains__("Facile"):
            rate = randint(20, 30)
        elif difficulty.__contains__("Moyen"):
            rate = randint(50, 60)
        elif difficulty.__contains__("Difficile"):
            rate = randint(70, 75)

        self.root.destroy()

        tak_generated_solved, tak_generated_to_solve = generate_takuzu(size, rate)
        r = tk.Tk()
        tk_menu = TakuzuMenu(r, tak_generated_to_solve, f"Grille générée {size}x{size} - {difficulty}.")
        tk_menu.set_takuzu_solved(tak_generated_solved)



    def size_menu(self) -> None:
        global SIZE_MENU
        if SIZE_MENU:
            return
        SIZE_MENU = True
        submenu = tk.Toplevel(self.root)
        submenu.resizable(False, False)
        window_width, window_height  = 200, 280
        center_window(submenu, window_width, window_height)

        submenu.protocol("WM_DELETE_WINDOW", lambda p=submenu: self.on_closing_size_menu(p))
        submenu.title("Choix de la taille de la grille")

        parameters = ["Taille 4x4", "Taille 6x6", "Taille 8x8", "Taille 10x10"]
        submenu.config(background=MENU_BACKGROUND)
        for parameter in parameters:
            button = tk.Button(submenu, text=parameter, font=("Courrier", 15, 'bold'), bg="white", fg="black", command=lambda p=parameter, q=submenu: self.choose_size_parameter(p, q))
            button.pack(pady=10)


    def on_closing_size_menu(self, submenu : tk.Toplevel) -> None:
        global SIZE_MENU
        SIZE_MENU = False
        submenu.destroy()
    


    def difficulty_menu(self, size : int) -> None:
        global DIFFICULTY_MENU
        if DIFFICULTY_MENU:
            return
        DIFFICULTY_MENU = True
        submenu = tk.Toplevel(self.root)
        submenu.resizable(False, False)
        window_width, window_height  = 200, 230
        center_window(submenu, window_width, window_height)

        submenu.protocol("WM_DELETE_WINDOW", lambda p=submenu: self.on_closing_diff_menu(p))

        submenu.title("Choix de la difficulté")
        parameters = ["Facile", "Moyen", "Difficile"]
        submenu.config(background=MENU_BACKGROUND)
        for parameter in parameters:
            button = tk.Button(submenu, text=parameter, font=("Courrier", 15, 'bold'), bg="white", fg="black", command=lambda p=parameter, q=submenu, s=size: self.choose_diff_parameter(p, q, s))
            button.pack(pady=10)
        

    def on_closing_diff_menu(self, submenu : tk.Toplevel) -> None:
        global DIFFICULTY_MENU
        DIFFICULTY_MENU = False
        submenu.destroy()

    def random_grid_selection(self) -> None:
        self.size_menu()

    def choose_file(self) -> str:
        file_path = filedialog.askopenfilename(title="Sélectionner un fichier", filetypes=[("Fichiers texte", "*.txt")])

        return file_path
    
    def get_root(self) -> tk.Tk:
        return self.root

    






