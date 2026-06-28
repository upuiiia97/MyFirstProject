#Урок №15. ООП

#Задание 1
print("задание1")

class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

#данные наследуются от род класса
class Autobus(Transport):
    pass

autobus = Autobus("Renaul Logan", 180, 12)

print(f"Название автомобиля: {autobus.name} Скорость: {autobus.max_speed} Пробег: {autobus.mileage}")


#Задание 2
print("задание2")

class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"Вместимость одного автобуса {self.name} {capacity} пассажиров"


class Autobus(Transport):
    #по умолчанию 50
    def seating_capacity(self, capacity=50):
        
        return f"Вместимость одного автобуса {self.name}: {capacity} пассажиров"


bus = Autobus("Renaul Logan", 180, 12)

print(bus.seating_capacity())