import ast
from cmath import inf
import csv
from posixpath import split
from tabnanny import check
from tkinter import *

mainwindow = Tk()
#startwindow = Tk()
#incedentwindow = Tk()

sherchbox = Entry(mainwindow)
sherchbox.grid()

feilds = []
rows = []
data = []
info = {}

def start():
    Button(startwindow, text="daily report", command=main).grid()
    Button(startwindow, text="incedent report", command=incedent).grid()
    Button(startwindow, text="sherch for student", command=sherch).grid()

def main():
    Label(mainwindow, text="date").grid(row=2,column=2)
    Label(mainwindow, text="class").grid(row=1, column=3)
    Label(mainwindow, text="weather").grid()
    Button(mainwindow, text="submit", command=sherch).grid(row=3, column=2)

def incedent():
    Label(incedentwindow, text="date").grid() #entry icdent date
    Label(incedentwindow, text="name of student").grid()#link to incednt name
    Label(incedentwindow, text="nature of incednt").grid()
    Label(incedentwindow, text="addtonal info").grid()

def submit():
    entry = entry.get()
    entry2 = entry2.get()

def sherchoutput(info):
    Label(main, text= info[0])
    Label(main, text= info[1])
    Label(main, text= info[2])
    Label(main, text= info[3])

def sherch():
    with open("stuff.csv") as mainfile:
        csv.reader(mainfile)
        feilds = ast.literal_eval(str(next(mainfile).split(",")))
        for i in mainfile:
            rows.append(i)
    for i in rows:
        print(i)
        data.append(dict(zip(feilds, str(i).split(","))))
    print(feilds)
    print(rows)
    print(data)

    Check = sherchbox.get()
    for i in data:
        for e in i.values():
             if Check in e:
                 info = i
                 info = info.values()
                 print(info)
                 sherchoutput(info)
main()
