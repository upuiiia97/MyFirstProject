#Урок №13. Двумерные списки

#Задание 1


import random

#Размер матриц
rows = 10
cols = 10

#матрица1
matrix_1 = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(random.randint(-50, 100))
    matrix_1.append(row)

#матрица2
matrix_2 = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(random.randint(-50, 100))
    matrix_2.append(row)

#Сложение матриц
matrix_3 = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(matrix_1[i][j] + matrix_2[i][j])
    matrix_3.append(row)

# Вывод результатов
print("Матрица 1:")
for row in matrix_1:
    print(row)

print("\nМатрица 2:")
for row in matrix_2:
    print(row)

print("\nСумма матриц:")
for row in matrix_3:
    print(row)
