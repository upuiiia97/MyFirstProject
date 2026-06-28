#Урок №16. Классы и объекты

#Задание2

class Turtle:

    def __init__(self, x, y, s):
        if s <= 0:
            raise ValueError("Шаг s должен быть больше 0")
        self.x = x
        self.y = y
        self.s = s  # длина шага

    #Движение
    def go_up(self):
        self.y += self.s

    def go_down(self):
        self.y -= self.s

    def go_left(self):
        self.x -= self.s

    def go_right(self):
        self.x += self.s

    def evolve(self):
        
        self.s += 1

    def degrade(self):
        
        if self.s - 1 <= 0:
            raise ValueError("Нельзя уменьшить шаг: текущий s станет ≤ 0")
        self.s -= 1

    #Подсчёт ходов
    def count_moves(self, x2, y2):
        
        dx = abs(x2 - self.x)
        dy = abs(y2 - self.y)

        #Проверка
        if dx % self.s != 0 or dy % self.s != 0:
        
            return dx // self.s + dy // self.s
