#Урок №7. Строки

#Задание 1


s = input() #Введи слово
if s == s[::-1]:
    print("yes")
else:
    print("no")


#Задание 2


s = input() #Ввести слова с пробелами

result = ' '.join(s.split()) #Удаление лишних пробелов
print(result)