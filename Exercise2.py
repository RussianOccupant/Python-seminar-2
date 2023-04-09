#Петя и Катя

x = int(input('Введите сумму: '))
y = int(input("Введите проихведение: "))
for i in range(x):
    for j in range(y):
        if x == i + j and y == i * j:
            print(f'Эти два числа {i} и {j}')