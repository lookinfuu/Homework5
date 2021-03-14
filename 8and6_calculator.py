def calc(a=1, b=2, operation="+"):
    def add(a1, b1):
        return a1 + b1

    def remove(a1, b1):
        return a1 - b1

    def multiply(a1, b1):
        return a1 * b1

    def divide(a1, b1):
        return a1 / b1

    def exponentiation(a1, b1):
        return a1 ** b1

    def sqrt(a1, b1):
        return b1 ** (1 / a1)
    
    def remofdiv(a1, b1):
        return a1 % b1

    selector = {
        "+": add,
        "-": remove,
        "*": multiply,
        "/": divide,
        "^": exponentiation,
        "sqrt": sqrt,
        "%": remofdiv
        }

    return selector[operation](a, b)

print("""*********   Калькулятор   ********* 
Вводите ваш запрос в следующем виде:
"число операция число"
Пример правильного ввода: 3 * 7
Доступные операции: 
"+" - сложение 
"-" - вычитание
"*" - умножение
"/" - деление
"^" - возведение в степень
"sqrt" - корень по основанию числа (2 sqrt 4 = 2)
"%" - остаток от деления""")
n = True
while n:
    n = input("Введите ваш запрос (Enter - выход):")
    if n:
        ln = list(n.split())
        try:
            ln[0] = float(ln[0])
            ln[2] = float(ln[2])
        except ValueError:
            print("Проверьте правильность ввода.")
            continue
        except OverflowError:
            print("Числа слишком большие.")
            continue
        except IndexError:
            print("Проверьте правильность ввода и повторите снова.")
            continue
        if len(ln) == 3:
            if ln[1] == "+" or ln[1] == "-" or ln[1] == "*" or ln[1] == "/" or ln[1] == "^" or ln[1] == "sqrt" or ln[1] == "%":
                try:
                    answer = calc(ln[0], ln[2], ln[1])
                except ZeroDivisionError:
                    if ln[0] == 0:
                        print(f"{ln[0]} {ln[1]} {ln[2]} = indeterminate")
                    else:
                        print(f"{ln[0]} {ln[1]} {ln[2]} = inf")
                except OverflowError:
                    print("Результат слишком большой.")
                else:
                    print(f"{ln[0]} {ln[1]} {ln[2]} = {answer:.2f}")
            else:
                print(f"{ln[1]} - неизвестная операция.")
                continue
        else:
            print("Проверьте правильность ввода и повторите снова.")
            continue
    else:
        print("Увидимся...")