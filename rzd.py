from datetime import datetime
import sys
from PIL import Image, ImageDraw, ImageFont
im = Image.open("Рисунок1.jpg")
current_datetime = datetime.now().year


class Train():
    def __init__(self):
        self.FIO = ""
        self.ffrom = ""
        self.where = ""
        self.service = ""
        self.age = 0
        self.train = 0
        self.money = 0
        self.r = 0

    def FIO1(self, name):
        name.title()
        if name.isdigit():
            print("ФИО не может содержать цифры")
        else:
            self.FIO = name
            self.FIO.title()

    def city(self, city1, city2):
        city1.title()
        if city1.isdigit() and city2.isdigit():
            print("Названия городов не может содержать цифры")
        else:
            self.ffrom = city1
            self.where = city2

    def services(self, service):
        if service.isdigit():
            print("без цифр")
        else:
            service.title()
            self.service = service
            if service == "Да":
                self.money += 100
            elif service == "Нет":
                self.money += 0

    def price(self, age):
        age1 = current_datetime - age
        self.age = age1
        if self.age <= 1985:
            self.money += 500
        elif self.age >= 1995 and self.age <= 2005:
            self.money += 600
        else:
            self.money += 700

    def place(self, train):
        trains = list(range(0, 11))
        for i in trains:
            if train == i:
                mesto = trains.pop(trains.index(i))
        self.train = mesto

    def seal(self):
        try:
            tatras = Image.open("Рисунок1.jpg")
        except BaseException:
            print("Unable to load image")
            sys.exit(1)
        self.r += 1
        idraw = ImageDraw.Draw(tatras)
        text1 = self.FIO
        text2 = (f"{self.ffrom} - {self.where}")
        text4 = (f"Наличие сервиса: {self.service}")
        text5 = (f"Цена: {str(self.money)}")
        text6 = (f"Номер поезда: {str(self.train)}")

        font = ImageFont.truetype("calibri.ttf", size=32)

        idraw.text((80, 170), text1, font=font, fill="#1C0606")
        idraw.text((80, 210), text2, font=font, fill="#1C0606")
        idraw.text((80, 250), text4, font=font, fill="#1C0606")
        idraw.text((80, 290), text5, font=font, fill="#1C0606")
        idraw.text((80, 330), text6, font=font, fill="#1C0606")
        tatras.save(f"Рисунок1.png")
        self.money = 0


train = Train()
# train.FIO1(input("Введите ваше имя и фамилию: "))
# train.city(input("Откуда собираетесь ехать?: "), input("Куда собираетесь  ?:)
# train.services(input("Нужен ли сервис?(Да/Нет): "))
# train.ages(int(input("Сколько вам лет?: ")))
# train.train1(int(input("Какое место собираетесь занимать?: ")))
# train.ppprint()

# train.FIO1("Данил Сагайдашный")
# train.city("Москва", "Кострома")
# train.services("asdasf")
# train.price(17)
# train.place(5)
# train.seal()
