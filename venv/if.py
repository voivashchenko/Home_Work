a=int(input("Введите число A: "))
b=int(input("Введите число Б "))
if a==b:
    c=int(input("Еще введите число В, поскольку А =  Б "))
    d = a + c
    e = b - c
elif a > b:
    print("Свершилось!")
elif b > a:
    print("Да ну!")
if a == b:
    print("А если так?")
elif d > e:
        print("Свершилось!")
elif d < e:
        print("Да ну!")
