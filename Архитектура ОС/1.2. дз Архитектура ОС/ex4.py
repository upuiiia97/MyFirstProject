#Урок 4. float, int и арифметические операции.

#Задание 1.


#Ввод сторон прямоугольника
a = float(input("1 сторона: "))
b = float(input("2 сторона: "))

#Вычисление площади и периметра
area = a * b
perimeter = 2 * (a + b)

#Вывод результатов
print(f"Площадь: {area}")
print(f"Периметр: {perimeter}")


#Задание 2.


n = int(input("Введите пятизначное число: ")) #46275

units = n % 10
tens = (n // 10) % 10
hundreds = (n // 100) % 10
thousands = (n // 1000) % 10
ten_thousands = n // 10000

result = (tens ** units * hundreds) / (ten_thousands - thousands)

print(f"Результат: {result}")