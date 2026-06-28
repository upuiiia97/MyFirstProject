#Урок №16. Классы и объекты

#Задание1

class CashRegister:
    
    #текущее кол-во денег
    def __init__(self, initial_amount=0):
        
        self._balance = initial_amount
    
    #пополнить
    def top_up(self, X):
        
        self._balance += X
        print(f"Касса пополнена на {X}. Текущий баланс: {self._balance}")

    #Выводит, сколько целых тысяч осталось в кассе
    def count_1000(self):
        
        thousands = self._balance // 1000
        print(f"Целых тысяч в кассе: {thousands}")
        return thousands
   
    #Забрать X из кассы. Если денег недостаточно — выкинуть ошибку.
    def take_away(self, X):
        
        if X > self._balance:
            raise ValueError(f"Недостаточно денег в кассе! Баланс: {self._balance}, требуется: {X}")
        self._balance -= X
        print(f"Из кассы забрали {X}. Остаток: {self._balance}")


#Пример
if __name__ == "__main__":
    cash = CashRegister(5000)

    cash.top_up(5500)     
    cash.count_1000()     #кол-во тысяч

    cash.take_away(3000)  

    # Попытка снять больше, чем есть - ошибка
    try:
        cash.take_away(10000)
    except ValueError as e:
        print(f"Ошибка: {e}")