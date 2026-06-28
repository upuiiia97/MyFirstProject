#Урок №5. Логические и условные операторы

#Задание 1

print("Задание 1")

#чет/нечет
number = int(input("Введите целое число: "))

#число нечетное
if number % 2 != 0:
    print("число не является четным")

#число четное    
else:
    if number < 0:
        print("отрицательное четное число")
    elif number == 0:
        print("нулевое число")
    else:
        print("положительное четное число")    


#Задание 2

print("Задание 2")  

word = input("Введи любое слово (en): ")

VOWELS= 'aeiou'

consonant_count = 0
vowel_count = 0

#Кол-во гласных и согласных
for char in word:
    if char in VOWELS:
        vowel_count += 1 
    else:
        consonant_count += 1
print(f"Гласных: {vowel_count}, Согласных: {consonant_count}")        

#Проверка на наличие всех гласных и их кол-во
all_vowels = True
vowel_count = {}

for vowel in VOWELS:
    count = word.count(vowel)
    vowel_count[vowel] = count
    if count == 0:
        all_vowels = False
if not all_vowels:
        print(False)        
else:
    for vowel, count in vowel_count.items():
                     
        print(f"{vowel}: {count}")


#Задание 3

print("Задание 3")  

X = int(input())  # минимальная сумма
A = int(input())  # деньги Майкла
B = int(input())  # деньги Ивана


if A >= X and B >= X:
    print(2)
elif A >= X:
    print("Mike")
elif B >= X:
    print("Ivan")
elif A + B >= X:
    print(1)
else:
    print(0)