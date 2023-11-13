from takuzu import Takuzu

class GridParser:

    def __init__(self, filename : str) -> None:
        self.__filename = filename
    

    def get_filename(self) -> str:
        return self.__filename
    
    def set_filename(self, filename) -> None:
        self.__filename = filename

    def get_takuzu(self) -> Takuzu:
        try:
            file = open(self.__filename, "r")

            grid = []

            for line in file.readlines():
                grid.append([int(x) for x in line.replace("\n", '').replace("_", "-1").split(' ')])
            
            return Takuzu(grid)

        except Exception:
            print(f"[ERREUR] Impossible de récupérer une grille de Takuzu depuis le fichier '{self.__filename}'. Fichier invalide.")
            return None


