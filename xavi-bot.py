import csv
from tkinter import *
from tkcalendar import Calendar

mainwindow = Tk()
startwindow = Tk()
incedentwindow = Tk()

dateofincdent = Calendar(incedentwindow, selectmode='day', year = 2020, month = 5, day = 22)

def creader(): 
    file = open("stuff.csv")
    cav = csv.DictReader(file)
    print(cav)
    file.close()

def cwriter():
    file = open("stuff.csv")
    cav = csv.writer(file)
    file.close()

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
    
main()
