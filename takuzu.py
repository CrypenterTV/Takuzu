import copy

class Takuzu:

    def __init__(self, grid : list) -> None:
        self.__grid = grid
    
    def get_grid(self) -> list:
        return self.__grid
    
    def set_grid(self, grid : list) -> None:
        self.__grid = grid
    
    def row_is_unique(self, index : int) -> bool:

        for i in range(index):
            if self.__grid[index] == self.__grid[i]:
                return False
        
        return True
    
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
    

    def __resolution(self, takuzu, row, col):

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
    
    def solve(self):
        return self.__resolution(copy.deepcopy(self), 0, 0)
    
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
    


    
    

