import ast
import csv
from posixpath import split
from tkinter import *

mainwindow = Tk()
startwindow = Tk()
incedentwindow = Tk()

feilds = []
rows = []
data = []


def start():
    Button(startwindow, text="daily report", command=main).grid()
    Button(startwindow, text="incedent report", command=incedent).grid()
    Button(startwindow, text="sherch for student", command=sherch).grid()

def main():
    Label(mainwindow, text="date").grid(row=2,column=2)
    Label(mainwindow, text="class").grid(row=1, column=3)
    Label(mainwindow, text="weather").grid()
    Button(mainwindow, text="submit", command=submit).grid(row=3, column=2)

def incedent():
    Label(incedentwindow, text="date").grid() #entry icdent date
    Label(incedentwindow, text="name of student").grid()#link to incednt name
    Label(incedentwindow, text="nature of incednt").grid()
    Label(incedentwindow, text="addtonal info").grid()

def submit():
    entry = entry.get()
    entry2 = entry2.get()

def sherch():
    with open("stuff.csv") as mainfile:
        csv.reader(mainfile)
        feilds.append(str(next(mainfile).split(",")))
        for i in mainfile:
            rows.append(i)
    print(feilds)
    for e in rows: #splits the single list of rows and makes each row its own list
         md = ast.literal_eval(str(e.split(",")))
         data.append(dict(zip(feilds, md)))
    print(data)

sherch()
