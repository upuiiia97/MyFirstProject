#Урок №16. Классы и объекты

#Задание2
class Turtle:
    def __init__(self, x=0, y=0, s=1):
        self.x = x
        self.y = y
        self.s = s

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
            raise ValueError("Невозможно уменьшить шаг: s станет ≤ 0")
        self.s -= 1

    def count_moves(self, x2, y2):
        
        dx = abs(x2 - self.x)
        dy = abs(y2 - self.y)

        #Кол-во шагов по каждой оси
        steps_x = (dx + self.s - 1) // self.s if dx > 0 else 0
        steps_y = (dy + self.s - 1) // self.s if dy > 0 else 0

        return steps_x + steps_y

#запуск

if __name__ == "__main__":
    t = Turtle(0, 0, 2)
    print(f"Позиция: ({t.x}, {t.y}), шаг: {t.s}")
    
    t.go_right()
    t.go_up()
    print(f"После go_right и go_up: ({t.x}, {t.y})")
    
    t.evolve()  #s = 3
    print(f"После evolve: шаг = {t.s}")
    
    moves = t.count_moves(10, 7)
    print(f"Минимальное число ходов до (10, 7): {moves}")
    
    try:
        t.degrade()
        t.degrade()  
        t.degrade()
    except ValueError as e:
        print(f"Ошибка: {e}")
