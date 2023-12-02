from takuzu import Takuzu

"""
Classe prenant en constructeur un chemin de fichier et
permettant de récupérer une grille de Takuzu depuis
un fichier texte sous un format spécifique.

    + Gestion des erreurs et des invalidités de 
    grilles le cas échéant.
"""

class GridParser:

    def __init__(self, filename : str) -> None:
        self.__filename = filename

    # Fonction permettant la récupération d'une grille de Takuzu
    # depuis le fichier spécifié. Renvoie None en cas d'erreur.
    def get_takuzu(self) -> Takuzu:
        try:
            file = open(self.__filename, "r")

            grid = []

            for line in file.readlines():
                grid.append([int(x) for x in line.replace("\n", '').replace("_", "-1").split(' ')])
            
            # Vérification que la grille récupérée soit bien une grille de Takuzu.
            n_rows = len(grid)
            for row in grid:

                for element in row:

                    if not element in [0, 1, -1]: # La grille ne peut contenir que: 0, 1 ou -1.
                        raise Exception

                if n_rows != len(row): # La grille doit avoir autant de lignes que de colonnes. Toutes de la même taille.
                    raise Exception

            return Takuzu(grid)

        except Exception:
            print(f"[ERREUR] Impossible de récupérer une grille de Takuzu depuis le fichier '{self.__filename}'. Fichier invalide.")
            return None
        

    def get_filename(self) -> str:
        return self.__filename
    
    def set_filename(self, filename) -> None:
         self.__filename = filename


