#Урок №8. Списки

#Задание 1


n = int(input("Выбери кол-во чисел: "))

# Ввод чисел
arr = [int(input("Введи число: ")) for i in range(n)]

# Вывод в обратном порядке
for num in arr[::-1]:
    print(num)


#Задание 2


n = int(input("ВВеди число: "))
arr = list(map(int, input("Введи цифры через пробел: ").split()))

if n > 0:
    arr = [arr[-1]] + arr[:-1]

print(' '.join(map(str, arr)))


#Задание 3


m = int(input("максимальная масса лодки: ")) 
n = int(input("кол-во рыбаков: "))  

# пересчет веса рыбаков
weights = []
for i in range(n):
    weights.append(int(input()))

# Сортировка веса по возрастанию
weights.sort()


left = 0           # самый лёгкий
right = n - 1      # самый тяжёлый
boats = 0

while left <= right:
    # Попытка посадить самого лёгкого и самого тяжёлого вместе
    if left < right and weights[left] + weights[right] <= m:
        # Помещаются оба
        left += 1
        right -= 1
    else:
        # Помещается только самый тяжёлый
        right -= 1
    boats += 1

print(f"Минимальное кол-во лодок: {boats}")