#Урок №9. Множества

#Задание 1


n = int(input("кол-во чисел: "))
arr = list(map(int, input("Ввод чисел через пробел: ").split()))

unique_numbers = set(arr)

# Вывод кол-во различных чисел
print(len(unique_numbers))


#Задание 2


#первый список
n = int(input("Введи число1: "))
list1 = set()
for i in range(n):
    list1.add(int(input()))

#второй список
m = int(input("Введи число2: "))
list2 = set()
for i in range(m):
    list2.add(int(input()))

#пересечение множеств
intersection = list1 & list2

print(f"Кол-во общих чисел: {len(intersection)}")


#Задание 3


numbers = input("Ввод чисел через пробел: ").split()

seen = set()

for num in numbers:
    if num in seen:
        print(num, "YES")
    else:
        print(num, "NO")
        seen.add(num)