#Урок №10. Словари

#Задание 1



pets = {}

pet_name = input("Имя питомца: ")
pet_type = input("Вид питомца: ")
pet_age = int(input("Возраст питомца: "))
owner_name = input("Имя владельца: ")

pets [pet_name] = {

    'Вид питомца': pet_type, 
    'Возраст питомца': pet_age, 
    'Имя владельца': owner_name 
}

#склонение года
def get_age_word(age):
    if age % 100 in [11, 12, 13, 14]:
        return "лет"
    elif age % 10 == 1:
        return "год"
    elif age % 10 in [2, 3, 4]:
        return "года"
    else:
        return "лет"

#Информация из словаря
for pet_name in pets.keys():
    pet_info = pets[pet_name]
    
    # Получаем значения через values()
    values = list(pet_info.values())
    pet_type = values[0]
    pet_age = values[1]
    owner_name = values[2]
    
    # Определение склонения
    age_word = get_age_word(pet_age)
    
    
    print(f'Это {pet_type} по кличке "{pet_name}". Возраст питомца: {pet_age} {age_word}. Имя владельца: {owner_name}')


#Задание 2


my_dict = {}

for x in range(10, -6, -1):
    my_dict[x] = x ** x

print(my_dict)