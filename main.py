from tkinter import *
from PIL import Image, ImageTk
import datetime


class Person:
    def __init__(self,name,birthdate):
        self.name = name
        self.birthday = birthdate

    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthday.year
        return age


def AgeCalc():
    name = nameEntry.get()
    monthkey = (
        Person(name,datetime.date(int(yearEntry.get()),int(monthEntry.get()),int(dateEntry.get()))))

    textArea = Text(master=window,height=10,width=25)
    textArea.grid(column=1, row=6)
    answer = " Heyy {monkey}!!!. You are {age} years old!!! ".format(monkey=name, age=monthkey.age())
    textArea.insert(END, answer)


window = Tk()
window.title("Age Calculator")
window.config(padx=100,pady=100)

image=Image.open('birthday.jpg')
photo=ImageTk.PhotoImage(image)
label_image = Label(image=photo)
label_image.grid(column=1,row=0)

name = Label(text="Name")
name.grid(column=0,row=1)
nameEntry = Entry()
nameEntry.grid(column=1,row=1)

year = Label(text="Year")
year.grid(column=0,row=2)
yearEntry = Entry()
yearEntry.grid(column=1,row=2)

month = Label(text="Month")
month.grid(column=0,row=3)
monthEntry = Entry()
monthEntry.grid(column=1,row=3)

date = Label(text="Date")
date.grid(column=0,row=4)
dateEntry = Entry()
dateEntry.grid(column=1,row=4)


button = Button(window,text="Calculate Age",command=AgeCalc,bg="yellow")
button.grid(column=1,row=5)

window.mainloop()