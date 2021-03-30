"""Реализовать класс фотоаппарат с полями модель, корпус (пластик, металл), зум (1-32).
Класс должен содержать геттеры и сеттеры с проверкой значений,
а также метод str для корректного вывода информации об объекте (включает стоимость).
Реализовать метод Cost для расчета стоимости по формуле(Зум+15) * 10 для пластиковых (Зум + 15) * 15 для металических.
Реализовать класс наследник Цифровой фотоаппарат с уникальным полем пиксели.
Реализовать метод Cost для расчета стоимости по формуле(Зум+ пиксели) * 10 для пластиковых (Зум + пиксели) * 15 для металических
 а также метод str для корректного вывода информации об объекте (включает стоимость).
создать 2 объекта. фотоаппарат, цифровой фотоаппарат и вывести информацию об объектах"""


class Foto:

    def __init__(self, model, body, zoom):
        self.model = model
        self.__body = body
        self.__zoom = zoom

    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, value):
        if value == 'металл' or value == 'пластик':
            self.__body = value
        else:
            print("Ошибка, неверное значение корпуса!")

    @property
    def zoom(self):
        return self.__zoom

    @zoom.setter
    def zoom(self, value):
        if value in range(1, 33):
            self.__zoom = value
        else:
            print('Ошибка, значение зума вне диапазона!')


    def __str__(self):
        return f'фотоаппарат :модель:{self.model}, корпус:{self.__body}, зум:{self.__zoom}'

class Pixel(Foto):
    def __init__(self, model, body, zoom,  pixels):
        super().__init__(model, body, zoom)
        self.pixels = pixels

    def __str__(self):
        return f'цифровой фотоаппарат :модель:{self.model}, корпус:{self.body}, зум:{self.zoom}, пиксели:{self.pixels}'
       # super().__init__(model, body,zoom)


def cost(zoom, body):
    if zoom in range(1, 33) and body == 'металл':
        costfoto = (int(zoom)+15) * 15
    elif zoom in range(1, 33) and body == 'пластик':
        costfoto = (int(zoom) + 15) * 10

    else:
        costfoto = 'Ошибка! некоректные данные!'
    return costfoto

def newcost(zoom, body, pixels):
    if zoom in range(1, 33) and body == 'металл':
         newcost = (int(zoom) + int(pixels)) * 15
    elif zoom in range(1, 33) and body == 'пластик':
        newcost = (int(zoom) + int(pixels)) * 10
    else:
        newcost = 'Ошибка! некоректные данные!'
    return newcost

while True:
    type =input ("Выбирите тип фотоаппарата для ввода данных. 1-обычный, 2 - цифровой, любая клавиша для выхода ")
    if type == "1":
        model = input('Введите модель аппарата ')
        body = input("Введите материал аппарата ")
        zoom = int(input('Введите макс.зум аппарата '))
        foto = Foto('фотоаппарат', 'неопределен', 1)
        foto.model = model
        foto.body = body
        foto.zoom = zoom
        print(foto)
        print("стоимость фотоаппарата составляет ", cost(zoom, body), '$')

    elif type == '2':
        model = input('Введите модель аппарата ')
        body = input("Введите материал аппарата ")
        zoom = int(input('Введите макс.зум аппарата '))
        pixels = int(input('Введите количество пикселей '))
        pfoto = Pixel('цифровой фотоаппарат', 'материал', 1, 1)
        pfoto.model = model
        pfoto.body = body
        pfoto.zoom = zoom
        pfoto.pixels = pixels
        print(pfoto)
        print("стоимость цифрового аппарата  составляет ", newcost(zoom, body, pixels), '$')
    else:
        break





