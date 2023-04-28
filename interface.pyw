from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter.ttk import Checkbutton
from datetime import datetime
import tkinter.messagebox as mb
from PIL import Image, ImageTk
from rzd import *
import os
import webbrowser

train = Train()
window = Tk()
tab_control = ttk.Notebook()
style = ttk.Style()

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)


def callback(event):
    webbrowser.open_new("https://t.me/qwesasuke")


text_help1 = Label(
    tab3,
    text="Если есть вопросы обращайтесь по указанным данным",
    bg="#DCDCDC",
    font=(
        "helvetica",
         10))

text_help = Label(
    tab3,
    text="Телеграмм",
    fg="blue",
    cursor="hand2",
    bg="#DCDCDC",
    font=(
        "helvetica",
         15))
text_help1.pack()
text_help.pack()
text_help.bind("<Button-1>", callback)

im = Image.open("RZD2.png")

Rzgimg = PhotoImage(file="RZD2.png")
RzgLab = Label(tab1, image=Rzgimg, bg="#DCDCDC")
RzgLab.place(x=250, y=0)

image_file = Image.open("r1.png")
image_file = image_file.resize((400, 400), Image.ANTIALIAS)
vp_image = ImageTk.PhotoImage(image_file)
Label(tab2, image=vp_image, bg="#DCDCDC").place(x=0, y=0)

tab_control.add(tab1, text="Главная")
tab_control.add(tab2, text="Мой билет")
tab_control.add(tab3, text="Помощь")

window.geometry("400x400")
window.title("Покупка РЖД билета")
window["bg"] = "#DCDCDC"

place = Combobox(tab1, width=21)
place['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
place.current(1)
place.place(x=165, y=130)

text_place3 = Label(
    tab1,
    text="Пассажирское место:",
    font="helvetica",
    bg="#DCDCDC",
    fg="red")
text_place3.place(x=0, y=130)

place2 = Combobox(tab1, width=30)
years = list(range(1, 100))
place2['values'] = (years)
place2.current(1)
place2.place(x=110, y=100)

destination1 = Label(
    tab1,
    text="Место отбытия:",
    font="helvetica",
    bg="#DCDCDC",
    fg="red")
destination2 = Label(
    tab1,
    text="Место прибытия:",
    font="helvetica",
    bg="#DCDCDC",
    fg="red")

destination1.place(x=0, y=160)
destination2.place(x=0, y=190)

dest1 = Entry(tab1, width=30)
dest2 = Entry(tab1, width=28)
dest1.place(x=120, y=160)
dest2.place(x=130, y=190)

text_place1 = Label(
    tab1,
    text="Ваше ФИО:",
    font="helvetica",
    bg="#DCDCDC",
    fg="red")
text_place2 = Label(
    tab1,
    text="Ваш Возраст:",
    font="helvetica",
    bg="#DCDCDC",
    fg="red")

text_place1.place(x=0, y=70)
text_place2.place(x=0, y=100)

chk_state = BooleanVar(tab1)
chk_state.set(True)
chk = Checkbutton(tab1, text="Наличие сервиса", var=chk_state)
chk.place(x=0, y=220)

name1 = Entry(tab1, width=35)
name1.place(x=90, y=70)


def buying():
    mesto = format(int(place.get()))
    year = format(int(place2.get()))
    name = format(name1.get())
    services = format(chk_state.get())
    desrinatin1 = format(dest1.get())
    desrinatin2 = format(dest2.get())
    if services == "True":
        services = "Да"
    elif services == "False":
        services = "Нет"
    if name == "" or desrinatin1 == "" or desrinatin2 == "":
        msg = "Заполните все поля"
        mb.showwarning("Информация", msg)
    elif name.isdigit() or desrinatin2.isdigit() or desrinatin1.isdigit():
        msg1 = "Поле не может содержать цифры"
        mb.showerror("Информация", msg1)
    else:
        train.FIO1(name.title())
        train.city(desrinatin1.title(), desrinatin2.title())
        train.services(services)
        train.price(int(year))
        train.place(int(mesto))
        train.seal()
        msg2 = "Билет напечатан"
        mb.showinfo("Информация", msg2)


def update_time():
    time.config(text=f"{datetime.now():%H:%M:%S}")
    window.after(100, update_time)


time = Label(window, font=("helvetica", 15), bg="#DCDCDC")
time.pack(side=TOP)
update_time()

style.theme_create("yummy", parent="alt", settings={
    "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0]}},
    "TNotebook.Tab": {
        "configure": {"padding": [5, 1], "background": "#d2ffd2"},
        "map": {"background": [("selected", "#dd0202")],
                "expand": [("selected", [1, 1, 1, 0])]}}})

style.theme_use("yummy")


title = Label(
    tab1,
    text="Федеральная \n пассажирская компания",
    font="helvetica",
    bg="#DCDCDC")
title.place(x=0, y=0)


tab_control.pack(expand=1, fill='both')

title = Label(
    window,
    text=(f'Сервис предоставляется ООО "УФС"'),
    fg="black",
    bg="#DCDCDC")
title.pack(side=BOTTOM)


def printt():
    try:
        os.startfile((r'Рисунок1.png'))
    except BaseException:
        msg2 = "Билет еще не напечатан"
        mb.showinfo("Информация", msg2)


btn1 = Button(tab2, text="Посмотреть билет", font=(
    "Arial", 20), fg="white", bg="red", command=printt)
btn = Button(tab1, text="Купить билет на поезд", font=(
    "Arial", 20), fg="white", bg="red", command=buying)
btn.place(x=20, y=500, width=350, height=50)
btn1.place(x=20, y=500, width=350, height=50)
btn.pack(side=BOTTOM)
btn1.pack(expand=1)

style.configure("TNotebook", tabposition='n', padding=10)
window.mainloop()
