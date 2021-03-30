# Задача №4:
# Функция to_list() принимает неограниченное количество параметров.
# Обработайте их так, чтобы на выходе получить список из этих элементов
a=[]
def to_list(args):
    a.append(args)
    return a

while True:
    q = input(" Нажмите ENTER для ввода данных или 1 для выхода  ")
    if q == str(1):
        break
    else:
        d = input(' Введите элемент списка : ')
        to_list(d)

print(a)

