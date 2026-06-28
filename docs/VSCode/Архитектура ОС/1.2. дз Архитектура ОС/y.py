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