def read_file(road_to_file):
    text = ""
    try:
        datafile = open(road_to_file, 'rb')
        text = datafile.read().decode('utf-8')
        datafile.close()
    except PermissionError:
        print("Недостаточно прав для работы с файлом.")
    except FileNotFoundError:
        print("Неверный путь к файлу или такого файла не существует.")
    return(text)

def symbols(text):
    d = {}
    for i in text:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return(d)

def words(text):
    list_text = list(text.split())
    return(len(list_text))

def sentences(text):
    text = text.replace ("? ", ". ")
    text = text.replace ("! ", ". ")
    list_text = list(text.split(". "))
    return(len(list_text))

print("*********   Программа анализа текста   *********")
while True:
    text = input("Введите текст (Enter - взять данные из файла):")
    if not text:
        text = read_file(input("Укажите путь к файлу:"))
    if not text:
        print("Данных нет.\nПопробуйте снова.")
        continue
    print('Частота вхождения символов текст:')
    d = symbols(text)
    for i in d:
        print(f'{i}:{d[i]}')
    print(f'Количество слов в тексте:\n{words(text)}')
    print(f'Количество предложений в тексте:\n{sentences(text)}')
    break