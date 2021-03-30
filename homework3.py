# Задача №3:
# Напишите функцию change(lst), которая принимает список и меняет местами его первый и последний элемент.
# В исходном списке минимум 2 элемента.

import random
def randomList():
    a = []
    len_a = input(" введите длину списка:")
    for _ in range(int(len_a)):
        a.append(random.randint(-10, 10))
    return a

def change(lst):
    element_1= lst[0]
    element_end = lst[len(lst)-1]
    lst[0] = element_end
    lst[len(lst) - 1] = element_1
    return lst

list_first = randomList()
print(' первоначальный список:', list_first)
list_chaneg = change(list_first)
print(' измененный список:    ', list_chaneg)
