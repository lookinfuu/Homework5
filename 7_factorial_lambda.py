def x_in():
    while True:
        x = input("Введите число:")
        try:
            x = int(x)
        except ValueError:
            print(f"{x} - дробное число." if x.find('.') != -1 and x.count('.') == 1 else f"{x} - не число." if x else "Вы ничего не ввели.")
            continue
        except OverflowError:
            print(f"{x} - число слишком большое.")
            continue
        if x < 0:
            print("Число должно быть положительным.")
            continue
        break
    return(x)

print("*********   Вычисление факториала числа (рекурсия)   *********")
factorial = lambda a: a if a == 1 else a * factorial(a-1)
x = x_in()
if x != 0:
    try:
        print(f"{x}! = {factorial(x)}")
    except RecursionError:
        print(f"Ошбика памяти. (Ограниченность метода)")
else:
    print(f"{x}! = 1")