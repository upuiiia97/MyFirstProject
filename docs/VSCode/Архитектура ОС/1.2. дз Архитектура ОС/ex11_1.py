#Урок №11. Функции

#Задание 1


#функция для вычисления факториала
def get_factorial(n):

    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


try:
    input_num = int(input("Введите натуральное целое число: "))

    
    factorial_3 = get_factorial(input_num)
    
    print(f"Факториал числа {input_num} равен: {factorial_3}")

    result_list = []
    
    for i in range(factorial_3, 0, -1):
        
        current_fact = get_factorial(i)
        result_list.append(current_fact)

    print(f"Итоговый список: {result_list}")

except ValueError:
    print("Ошибка. Введите корректное число.")



