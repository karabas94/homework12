"""
Написать класс ITMan
аттрибуты:
    'firstname': 'Ivasik',
    'lastname': 'Telesik',
    'age': 13,
    'e-mail': 'ivasik-telesik1732@izkrnanog.ua',
    'skils': ['ходить', "говорить", "кодить"],
    'people_lang': ['Україньська', "Англійська"],
    'coding_lang': ['Python', "C++", "lisp"],
методы на свое усмотрение(удобство оценивается)

со звездочкой
добавить возможность добавления объектов класса в список
добавить инструментарий хранения этого списка в файле(JSON) между запусками программы
"""
import json


# creating class of IT people
class ITMan:
    def __init__(self):
        self.firstname = str(input("Enter Name: "))
        self.lastname = str(input("Enter Last name: "))
        self.age = int(input("Enter Age: "))
        self.e_mail = str(input("Enter E-mail: "))
        self.skills = str.split(input("Enter skills: "))
        self.people_lang = str.split(input("Enter speaking languish: "))
        self.coding_lang = str.split(input("Enter IT languish:"))

    def __str__(self):
        return f'Firstname: {self.firstname}, Lastname: {self.lastname}, Age: {self.age}, E-mail: {self.e_mail}, ' \
               f'Skills: {self.skills}, Speaking languish: {self.people_lang}, IT languish: {self.coding_lang}'


# creating and appending instances to list
li = [ITMan().__str__()]
# appending list with dude to json format
with open("stat.txt", "a") as file:
    json.dump(li, file)
