"""Задача №5:
Дмитрий считает, что когда текст пишут в скобках (как вот тут, например), его читать не нужно.
Вот и надумал он существенно укоротить время чтения, написав функцию, которая будет удалять все, что расположено внутри скобок.
Помогите ленивому Диме разработать функцию shortener(st),
которая будет удалять все, что внутри скобок и сами эти скобки, возвращая очищенный текст (скобки могут быть вложенными).
"""


def read_file(name_file):       # функция чтения файла
    file = open(name_file, 'r', encoding='windows-1251')
    data = file.read()
    file.close()
    return data


def write_file(name_file,value):     # функция записи файла
    file = open(name_file, 'w',encoding='windows-1251')
    data = file.write(value)
    file.close()
    return data



def clear(name_file):               # функция очистки ()
    while True:
        text_a = read_file(name_file)
        begin = int(text_a.find('('))           # поиск индекса первой открытой скобки
        if begin != -1:                         # если найдена скобка то
            end = int(text_a.find(')'))         # поиск первой закрытой скобки

            text_b = text_a[begin:end + 1]      # text_b = срез в скобках

            beginb = int(text_b.rfind('('))     # поиск первой открытой скобки в срезе
            endb = int(text_b.find(')'))        # поиск последней закрытой скобки в срезе

            text_c = text_b[beginb:endb + 1]    # text_c = новый срез

            new_a = text_a.replace(text_c, '')  # замена среза на ''

            write_file(name_file, new_a)        # перезапись файла
        else:
            break

print('Исходный текст:','\n', read_file('text5.txt'))
clear('text5.txt')
print('Исправленный текст','\n', read_file('text5.txt'))


