#Урок №11. Функции

#Задание 2


import collections

#словарь с питомцами
pets = {
    1: {
        "Мухтар": {
            "Вид питомца": "Собака",
            "Возраст питомца": 9,
            "Имя владельца": "Павел"
        },
    },
    2: {
        "Каа": {
            "Вид питомца": "желторотый питон",
            "Возраст питомца": 19,
            "Имя владельца": "Саша"
        },
    },
}

# проверка инф о питомце
def get_pet(ID):
    
    return pets[ID] if ID in pets.keys() else False

#склонение года
def get_suffix(age):
    
    age = abs(int(age))
    
    if age % 100 in [11, 12, 13, 14]:
        return "лет"
    elif age % 10 == 1:
        return "год"
    elif age % 10 in [2, 3, 4]:
        return "года"
    else:
        return "лет"
    
#Выводит список всех питомцев из бд
def pets_list():
    
    if not pets:
        print("База данных пуста.")
        return
        
    for ID, pet_data in pets.items():
        
        name = list(pet_data.keys())[0]
        details = pet_data[name]
        
        suffix = get_suffix(details["Возраст питомца"])
        
        print(f'Это {details["Вид питомца"]} по кличке "{name}". '
              f'Возраст питомца: {details["Возраст питомца"]} {suffix}. '
              f'Имя владельца: {details["Имя владельца"]}')

#Основные функции

def create():

    last = collections.deque(pets, maxlen=1)[0] if pets else 0
    new_id = last + 1
    
    print(f"\nДобавление питомца. Новый ID: {new_id}")
    name = input("Имя питомца: ")
    kind = input("Вид питомца: ")
    age = int(input("Возраст питомца: "))
    owner = input("Имя владельца: ")
    
    pets[new_id] = {
        name: {
            "Вид питомца": kind,
            "Возраст питомца": age,
            "Имя владельца": owner
        }
    }
    print(f"Питомец {name} успешно добавлен с ID {new_id}!")


def read():
    
    ID = int(input("\nВведите ID питомца для чтения: "))
    pet = get_pet(ID)
    
    if pet:
        name = list(pet.keys())[0]
        details = pet[name]
        suffix = get_suffix(details["Возраст питомца"])
        
        print(f'\nЭто {details["Вид питомца"]} по кличке "{name}". '
              f'Возраст питомца: {details["Возраст питомца"]} {suffix}. '
              f'Имя владельца: {details["Имя владельца"]}')
    else:
        print(f"Питомец с ID {ID} не найден в базе данных.")


def update():
    
    ID = int(input("\nВведите ID питомца для обновления: "))
    pet = get_pet(ID)
    
    if pet:
        name = list(pet.keys())[0]
        details = pet[name]
        print(f"Обновление данных для питомца {name} (ID: {ID})")
        
        #вносим новые данные 
        kind = input(f'Новый вид питомца [{details["Вид питомца"]}]: ') or details["Вид питомца"]
        age_input = input(f'Новый возраст [{details["Возраст питомца"]}]: ')
        age = int(age_input) if age_input else details["Возраст питомца"]
        owner = input(f'Новое имя владельца [{details["Имя владельца"]}]: ') or details["Имя владельца"]
        
    
        pets[ID] = {
            name: {
                "Вид питомца": kind,
                "Возраст питомца": age,
                "Имя владельца": owner
            }
        }
        print("Данные успешно обновлены!")
    else:
        print(f"Питомец с ID {ID} не найден в базе данных.")


def delete():
    
    ID = int(input("\nВведите ID питомца для удаления: "))
    
    if get_pet(ID):
        del pets[ID]
        print(f"Питомец с ID {ID} успешно удален.")
    else:
        print(f"Питомец с ID {ID} не найден в базе данных.")


#основной цикл программы

command = ""
print("База данных ветеринарной клиники")

while command != 'stop':
    print("\nМЕНЮ")
    print("create - создать запись")
    print("read - просмотреть запись")
    print("update - обновить запись")
    print("delete - удалить запись")
    print("list - показать всех питомцев")
    print("stop - выйти из программы")
    
    command = input("Введите команду: ").strip().lower()
    
    if command == 'create':
        create()
    elif command == 'read':
        read()
    elif command == 'update':
        update()
    elif command == 'delete':
        delete()
    elif command == 'list':
        pets_list()
    elif command == 'stop':
        print("Программа завершена.")
    else:
        print("Неизвестная команда. Попробуйте еще раз.")