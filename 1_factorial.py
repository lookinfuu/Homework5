def factorial(number):
    l = list(range(1,number + 1))
    for i in range(0, len(l) - 1):
        l[i + 1] = l[i] * l[i + 1]
    return(l[-1])

number = input("Введите число:")
try:
    number = int(number)
except ValueError:
    print(f"{number} - дробное число." if number.find('.') != -1 and number.count('.') == 1 else f"{number} - не число." if number else "Вы ничего не ввели.")
except MemoryError:
    print("Не сегодня...")
except OverflowError:
    print(f"{number} - число слишком большое.")
if number < 0:
    print("Число должно быть положительным")
elif number == 0:
    print(f"{number}! = 1")
else:
    answer = factorial(number)
    print(f"{number}! = {answer}")