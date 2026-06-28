# Урок №6. Циклы while и for

#Задание 1


#Ввод чисел
N = int(input())

zero_count = 0

#Подсчет нулей
for i in range(N):
    num = int(input())
    if num == 0:
        zero_count += 1

print(f"Чисел равно 0: {zero_count}")        


#Задание 2


import math

x = int(input())
count = 0

for i in range(1, int(math.isqrt(x)) + 1): #целочисленный квадратный корень
    if x % i == 0:
        count += 1  
        if i != x // i:
            count += 1 
print(count)

#Задание 3


# Ввод чисел A и B через пробел
a, b = map(int, input().split())

if a % 2 != 0:
    a += 1

# Вывод всех чётных чисел от a до b
for i in range(a, b + 1, 2):
    print(i, end=' ')