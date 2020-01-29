a=int(input("Введите число A: "))
b=int(input("Введите число Б "))
c=int(input("Введите число B "))
while (a + c) <= b:
    print(a + c, "Пока что нет")
    a = a + c
    if (a + c) > b:
        print('Дождались!', a + c)