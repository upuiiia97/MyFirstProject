# 0 - поле
# 1 - дерево
# 2 - река
# 3 - госпиталь
# 4 - апгрейд шоп

CELL_TYPES = "🟩🌲🌊🏥🏦"

class Map:
    # def generate_rivers():

    def generate_forest():

    def print_map(self):
        print("⬛️" * (self.w + 2))   #верхняя рамка
        for row in self.sells:
            print("⬛️", end="")  #первый и последний черный квадрат
            for cell in row:
                if (cell >= 0 and cell < len(CELL_TYPES)):
                    print(CELL_TYPES[cell], end="")                  
            print("⬛️")                  
        print("⬛️" * (self.w + 2))      #нижняя рамка

    def check_bounds(self, x, y):   #проверка соблюдения условий
        if (x < 0 or y < 0 or x >= self.h or y >= self.w):
            return False
        return True        


    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.sells = [[0 for i in range(w)] for j in range(h)]

tmp = Map(10, 10)   #размеры карты


if (tmp.check_bounds(2, 3)):
    print("YES")

tmp.print_map()
