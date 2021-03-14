def a_in():
    while True:
        a = input("Введите ежемесячный взнос:")
        try:
            a = float(a)
        except ValueError:
            print(f"{a} - не число." if a else "Вы ничего не ввели.")
            continue
        except OverflowError:
            print(f"{a} - число слишком большое.")
            continue
        else:
            break
    return(a)

def b_in():
    while True:
        b = input("Введите ежемесячный банковский процент:")
        try:
            b = float(b)
        except ValueError:
            print(f"{b} - не число." if b else "Вы ничего не ввели.")
            continue
        except OverflowError:
            print(f"{b} - число слишком большое.")
            continue
        else:
            break
    return(b)

def c_in():
    while True:
        c = input("Введите срок накоплений в месяцах:")
        try:
            c = int(c)
        except ValueError:
            print(f"{c} - дробное число." if c.find('.') != -1 and c.count('.') == 1 else f"{c} - не число." if c else "Вы ничего не ввели.")
            continue
        except OverflowError:
            print(f"{c} - число слишком большое.")
            continue
        else:
            break
    return(c)

def bank(a,b,c):
    cash = a
    your_cash = 0
    bank_cash = 0
    for i in range(0,c):
        your_cash += a
        bank_cash += cash * b / 100
        cash = cash + cash * b / 100
        if c - i != 1:
            cash = cash + a
    return(cash, your_cash, bank_cash)

def last_symbols(c):
    c = str(c)
    l = list(c)
    ls = int(l[-1])
    if len(l) > 1:
        ls2 = int(l[-2])
        if ls2 == 1:
            flag = 3
        else:
            if ls == 1:
                flag = 1
            elif ls == 2 or ls == 3 or ls == 4:
                flag = 2
            else:
                flag = 3
    else:
        if ls == 1:
            flag = 1
        elif ls == 2 or ls == 3 or ls == 4:
            flag = 2
        else:
            flag = 3
    return(flag)

print("*********   Программа 18+   *********")
a = a_in()
b = b_in()
c = c_in()
f = last_symbols(c)
list_cash = bank(a,b,c)
cash = list_cash[0] 
your_cash = list_cash[1]
bank_cash = list_cash[2]
universe = ""
if c > 2400:
    cash = cash * 10 ** (-150)
    universe = True
print(f"Итоговая сумма, спустя {c} месяц{'' if f == 1 else 'а' if f == 2 else 'eв'}: {cash:.2f} {'' if not universe else 'intergalactic pennies'}")
print(f"За все время:\nВы внесли: {your_cash:.0f}\nБанк вам начислил: {bank_cash:.2f}")