import tkinter as tk
from tkinter import ttk, font, Menu, messagebox
from takuzu import Takuzu
from gridparser import GridParser
import main_menu
import subprocess
import sys
import copy




class TakuzuMenu:

    def __init__(self, root : tk.Tk, takuzu : Takuzu, filename : str) -> None:

        self.root = root
        
        self.takuzu = takuzu

        self.filename = filename

        self.initial_takuzu = copy.deepcopy(self.takuzu)

        self.takuzu_solved = None

        self.labels = []

        self.red_labels = []

        self.root.title(f"Jeu du Takuzu : {filename}")
        self.root.resizable(False, False)
        table = tk.Frame(self.root)
        table.grid(row=0, column=0)

        custom_font = font.nametofont("TkDefaultFont")
        custom_font.configure(size=20)


        unsolved_label_frame = tk.LabelFrame(table, text=filename)
        unsolved_label_frame.grid(row=0, column=0)
        self.create_label_grid(unsolved_label_frame)

        self.create_menu_bar()

        root.update_idletasks()
        
        main_menu.center_window(root, root.winfo_width(), root.winfo_height(), 25)

        root.protocol("WM_DELETE_WINDOW", self.on_closing)


    

    def create_label_grid(self, parent):
        custom_font = font.nametofont("TkDefaultFont")
        custom_font.configure(size=20)

        for i in range(len(self.takuzu.get_grid())):

            row_labels = []
            for j in range(len(self.takuzu.get_grid())):
                text = self.takuzu.get_grid()[i][j]
                text_color = "#ed9511"
                if text == -1:
                    text = '_'  
                    text_color = "black"  
                label = tk.Label(parent, text=f"{text}", fg=text_color, width=4, height=2, borderwidth=1, relief="solid", font=custom_font)
                label.grid(row=i, column=j)
    
                label.bind("<Button-1>", lambda event, i=i, j=j: self.on_label_click(i, j))
                row_labels.append(label)

            self.labels.append(row_labels)


    def create_menu_bar(self):
        menu_bar = Menu(self.root)

        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Ouvrir", command=self.open_new_grid)
        file_menu.add_command(label="Enregistrer", command=self.save_grid)
        file_menu.add_separator()
        file_menu.add_command(label="Retour au menu", command=self.on_return_menu)
        file_menu.add_command(label="Quitter", command=self.on_closing)


        edit_menu = Menu(menu_bar, tearoff=0)
        edit_menu.add_command(label="Résoudre", command=self.solve_grid)
        edit_menu.add_command(label="Réinitialiser", command=self.reset_grid)


        menu_bar.add_cascade(label="Fichier", menu=file_menu)
        menu_bar.add_cascade(label="Grille", menu=edit_menu)


        self.root.config(menu=menu_bar)




    def solve_grid(self):
        if self.takuzu_solved == None:
            self.takuzu_solved = self.initial_takuzu.solve()

        if self.takuzu_solved == None:
            messagebox.showerror("Erreur", "La grille de départ n'est pas résoluble !")
            return
        
        for i in range(len(self.takuzu_solved.get_grid())):
            for j in range(len(self.takuzu_solved.get_grid())):
                text = self.takuzu_solved.get_grid()[i][j]
                if text == -1:
                    text = '_'
                self.labels[i][j].config(text=f"{text}")


    def reset_grid(self):
        for i in range(len(self.initial_takuzu.get_grid())):
            for j in range(len(self.initial_takuzu.get_grid())):
                self.takuzu.get_grid()[i][j] = self.initial_takuzu.get_grid()[i][j]
                text = self.initial_takuzu.get_grid()[i][j]
                if text == -1:
                    text  = '_'
                self.labels[i][j].config(text=f"{text}", fg="black")



    def on_label_click(self, i, j):
        # Ordre: [_, 0, 1]
        label_clicked = self.labels[i][j]
        #print(self.initial_takuzu.get_grid()[i][j])
        if self.initial_takuzu.get_grid()[i][j] != -1:
            return
        current_text = label_clicked.cget("text")
        new_text = ''
        order = ['_', '0', '1']
        if str(current_text) in order:
            new_text = order[(order.index(current_text) + 1) % 3]
        
        if new_text == '_':
            self.takuzu.get_grid()[i][j] = -1
        else:
            self.takuzu.get_grid()[i][j] = int(new_text)

        if new_text == '_':
            label_clicked.config(text=new_text, fg="black")
            return

        if self.takuzu.is_valid():
            label_clicked.config(text=new_text, fg="blue")
            for label in self.red_labels:
                label.config(fg="blue")
            self.red_labels.clear()

        else:
            label_clicked.config(text=new_text, fg="red")
            self.red_labels.append(label_clicked)
        

        #Si la grille est résolue par l'utilisateur
        if self.takuzu.is_completely_solved():
            for row_label in self.labels:
                for label in row_label:
                    label.config(fg="green")
            messagebox.showinfo("Félicitations !", "Vous avez résolu la grille avec succès !")
        

    def open_new_grid(self):
        print("Fonction d'ouverture d'une nouvelle grille...")

    def save_grid(self):
        print("Fonction de sauvegarde de la grille actuelle...")


    def on_closing(self):
        if messagebox.askokcancel("Fermeture", "Voulez vous quitter le programme ? \nAttention: Tous les éléments non sauvegardés seront perdus."):
            self.root.destroy()
            exit(0)
    
    def on_return_menu(self):
        if messagebox.askokcancel("Retour au Menu", "Voulez vous retourner au menu ? \nAttention: Tous les éléments non sauvegardés seront perdus."):
            self.root.destroy()
            subprocess.run([sys.executable, "main.py"])


            


        

