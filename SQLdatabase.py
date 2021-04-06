""" Создать базу данных для преподавателей и студентов, с возможностью добавления, просмотра и редактирования данных,
пароль необходимо шифровать"""

"""import pymysql
from pymysql.cursors import DictCursor


class DataBase:
    def __init__(self):
        self.connection = self.connect()
        self.cursors = self.connection.cursor()

    def connect(self):
        connection = pymysql.connect(
            host='localhost',
            user='admin',
            password='qwerty123',
            db='un',
            charset='utf8mb4',
            cursorclass=DictCursor
        )
        return connection

    def addUser(self, login, password):
        sql = "INSERT INTO users (id, login, password) VALUES (%s, %s, %s)"
        temp = [3, login, password]
        self.cursors.execute(sql, temp)
        self.connection.commit()""""




# Start
print(" Добро пожаловать в систему")

enter = input (" Нажмите 1 для входа в систему или 2 для регистрации ")
'''while True:
    if enter =="1":
        pass
    elif enter =="2":
        pass
    else:
        break'''

def password():
    while True:
        login = input(' Введите логин (не менее 6 символов)')
        if len(login) < 6:
            print(" Пароль должен быть больше 6 символов")
        else:

    password = input(" Введите пароль (не менее 6 символов)")



def registr():
    type = input(" Если Вы преподаватель, нажмите 1, если студент нажмите 2 ")
    name = input(" Введите имя ")
    theme = ''
    lastname = input (" Введите фамилию ")
    faculty  = input (" Введите факультет ")
    if type == "1":
        theme = input ("Введите предмет " )
    elif type == "2":
        theme = input(" Введите номер группы")

    login = input (' Введите логин (не менее 6 символов)')
    password = input (" Введите пароль (не менее 6 символов)")
    return type, name, lastname, faculty, theme, login, password

print(registr())

