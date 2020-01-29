a=int(input("Введите число A: "))
b=int(input("Введите число Б "))
if a==b:
    c=int(input("Еще введите число В, поскольку А =  Б "))
    d = a + c
    e = b - c
if a > b:
    print("Свершилось!")
if b > a:
    print("Да ну!")
if a == b:
    print("А если так?")
    if d > e:
        print("Свершилось!")
    if d < e:
        print("Да ну!")