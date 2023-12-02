import copy
from random import shuffle, random

# Classe principale modélisant une grille de Takuzu.

class Takuzu:

    def __init__(self, grid : list) -> None:
        self.__grid = grid
    
    # Fonction permettant de vérifier l'unicité d'une ligne dans la grille.
    def row_is_unique(self, index : int) -> bool:

        for i in range(index):
            if self.__grid[index] == self.__grid[i]:
                return False
        
        return True
    
    # Fonction permettant de vérifier la validé d'une colonne :
    def col_is_valid(self, index : int) -> bool:

        counter_0, counter_1 = 0, 0
        is_complete = True
        for i in range(len(self.__grid)):
            if self.__grid[i][index] == 0:
                counter_0 += 1
            elif self.__grid[i][index] == 1:
                counter_1 += 1
            else:
                is_complete = False
            if i > 1:
                if self.__grid[i-2][index] == self.__grid[i-1][index] == self.__grid[i][index] != -1:
                    return False
        
        if len(self.__grid) / 2 == counter_1:
            return True
        if not is_complete:
            return counter_1 <= len(self.__grid) / 2
        

    def row_is_valid(self, index : int) -> bool:

        counter_0, counter_1 = 0, 0
        is_complete = True
        for i in range(len(self.__grid)):
            if self.__grid[index][i] == 0:
                counter_0 += 1
            elif self.__grid[index][i] == 1:
                counter_1 += 1
            else:
                is_complete = False
            
            if i > 1:
                if self.__grid[index][i-2] == self.__grid[index][i-1] == self.__grid[index][i] != -1:
                    return False
                
        if len(self.__grid) / 2 == counter_0 == counter_1:
            return True
        if not is_complete:
            return counter_0 <= len(self.__grid) / 2 and counter_1 <= len(self.__grid) / 2
        

    def is_valid(self) -> bool:

        for i in range(len(self.__grid)):
            if not (self.row_is_valid(i) and self.row_is_unique(i)):
                return False
            
            for j in range(len(self.__grid)):
                if not(self.col_is_valid(j) and self.row_is_unique(j)):
                    return False
        return True
    


    # Fonction permettant de vérifier si une grille est totalement completée et valide.
    def is_completely_solved(self) -> bool:

        if not self.is_valid():
            return False
        
        for row in self.__grid:
            # Renvoi False si la grille contient autre chose que des 0 ou des 1.
            for n in row: 
                if (not n == 0) and (not n == 1): 
                    return False
                
        return True


    def __resolution(self, takuzu : 'Takuzu', row : int, col : int):

        for i in [0,1]:

            if self.__grid[row][col] == -1:
                takuzu.get_grid()[row][col] += 1
            
            if col < len(self.__grid[row]) - 1:

                if takuzu.row_is_valid(row) and takuzu.col_is_valid(col):
                    new_takuzu = self.__resolution(copy.deepcopy(takuzu), row, col + 1)
                    if new_takuzu != None and new_takuzu.is_valid():
                        return new_takuzu
                
            elif row < len(self.__grid) - 1:

                if takuzu.row_is_valid(row) and takuzu.col_is_valid(col) and takuzu.row_is_unique(row):
                    new_takuzu = self.__resolution(copy.deepcopy(takuzu), row + 1, 0)
                    if new_takuzu != None and new_takuzu.is_valid():
                        return new_takuzu
            
            else:
                if takuzu.is_valid():
                    return takuzu
                return None
        
        return None
    
    def solve(self) -> 'Takuzu':
        return self.__resolution(copy.deepcopy(self), 0, 0)
    
    # Fonction permettant de représenter la grille de Takuzu sous forme 
    # d'une chaîne de caractères.
    def __str__(self) -> str:
        
        f_string = "-"*(len(self.__grid)*3 + 2) + "\n"
        for line in self.__grid:
            sb = "| "
            for i in range(len(line)):
                spaces = ""
                if i != len(line) - 1:
                    spaces += "  "

                if line[i] == -1:
                    sb += "_" + spaces
                else:
                    sb += str(line[i]) + spaces 
            sb += " |"
            f_string += sb + "\n"
            
        f_string += "-"*(len(self.__grid)*3 + 2) + "\n"

        return f_string
    

    # Fonction permettant de convertir la grille de Takuzu en chaîne de caractères sous le format 
    # adéquat pour l'enregistrment dans un fichier texte (destinée à être analysée par le parser).
    def convert_to_text_file(self) -> str:
        sb = ""
        for i in range(len(self.__grid)):

            for j in range(len(self.__grid)):
                text = str(self.__grid[i][j])

                if text == "-1":
                    text = "_"

                sb += text
                # Ne pas rajouter d'espace à la fin de la ligne.
                if j < len(self.__grid) - 1:
                    sb += " "

            # Ne pas rajouter d'espace en dessous de la dernière ligne.
            if i < len(self.__grid) - 1:
                sb += "\n"

        return sb
                
    def permute_columns(self) -> None:
        num_columns = len(self.__grid[0])
        
        column_indices = list(range(num_columns))

        shuffle(column_indices)

        for row in self.__grid:

            new_row = []

            for i in column_indices:
                new_row.append(row[i])
            row[:] = new_row

    def get_grid(self) -> list:
        return self.__grid
    
    def set_grid(self, grid : list) -> None:
        self.__grid = grid

def generate_takuzu(n: int, rate : float) -> Takuzu:
    assert n > 0 and n % 2 == 0
    assert 0 <= rate <= 100

    takuzu = Takuzu([[-1 for _ in range(n)] for _ in range(n)])

    takuzu_solved = takuzu.solve()

    shuffle(takuzu_solved.get_grid())
    takuzu_solved.permute_columns()

    while not takuzu_solved.is_valid():
        shuffle(takuzu_solved.get_grid())
        takuzu_solved.permute_columns()
    
    takuzu_to_solve = copy.deepcopy(takuzu_solved)

    for i in range(len(takuzu_to_solve.get_grid())):
        for j in range(len(takuzu_to_solve.get_grid())):
            if random() * 100 < rate:
                takuzu_to_solve.get_grid()[i][j] = - 1

    return (takuzu_solved, takuzu_to_solve)