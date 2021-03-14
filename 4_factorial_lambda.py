from functools import reduce

def number_in():
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

print("*********   Вычисление факториала числа (не рекурсия)   *********")
step = lambda a: [i for i in range(1,a + 1)]
x = number_in()
if x != 0:
    sp = step(x)
    factorial = reduce(lambda c, d: c * d, sp)
    print(f"{x}! = {factorial}")
else:
    print(f"{x}! = 1")