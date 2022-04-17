import ast
import csv
from tkinter import *

startwindow = Tk()

dropvalues = ["student", "location"]
sherchby = StringVar()


feilds = []
rows = []
data = []
info = {}


def start():
    Button(startwindow, text="daily report", command=daliyreportwindow).grid()
    Button(startwindow, text="sherch", command=main).grid()
    Button(startwindow, text="add student", command=addstudentwindow).grid()


def main():
    mainwindow = Tk()
    OptionMenu(mainwindow, sherchby, *dropvalues).grid(row=1, column=2)
    Label(mainwindow, text="sherch by").grid(row=1, column=1)
    Label(mainwindow, text="sherch for").grid(row=2, column=1)
    Button(mainwindow, text="submit", command=sherch).grid(row=3, column=2)
    global sherchbox
    sherchbox = Entry(mainwindow)
    sherchbox.grid(row=2, column=2)


def addstudentwindow():
    def makelist():
        global newstudent
        newstudent = [studentbox1.get(), studentbox2.get(), studentbox3.get()]
        write()
    mainwindow = Tk()
    global writeas
    writeas = "role.csv"
    Label(mainwindow, text="student name").grid(row=1, column=1)
    studentbox1 = Entry(mainwindow)
    studentbox1.grid(row=1, column=2)
    Label(mainwindow, text="student age").grid(row=2, column=1)
    studentbox2 = Entry(mainwindow)
    studentbox2.grid(row=2, column=2)
    Label(mainwindow, text="student class").grid(row=3, column=1)
    studentbox3 = Entry(mainwindow)
    studentbox3.grid(row=3, column=2)
    Button(mainwindow, text="subimt", command=makelist).grid(row=4, column=2)


def daliyreportwindow():
    def makelist():
        global reportdata
        reportdata = [
            reportbox1.get(),
            reportbox2.get(),
            reportbox3.get(),
            reportbox4.get(),
            reportbox5.get()]
        write()
    mainwindow = Tk()
    global writeas
    writeas = "stuff.csv"
    Label(mainwindow, text="location").grid(row=1, column=1)
    reportbox1 = Entry(mainwindow)
    reportbox1.grid(row=1, column=2)
    Label(mainwindow, text="number of students").grid(row=2, column=1)
    reportbox2 = Entry(mainwindow)
    reportbox2.grid(row=2, column=2)
    Label(mainwindow, text="day").grid(row=3, column=1)
    reportbox3 = Entry(mainwindow)
    reportbox3.grid(row=3, column=2)
    Label(mainwindow, text="weather").grid(row=4, column=1)
    reportbox4 = Entry(mainwindow)
    reportbox4.grid(row=4, column=2)
    Label(mainwindow, text="class").grid(row=5, column=1)
    reportbox5 = Entry(mainwindow)
    reportbox5.grid(row=5, column=2)
    Button(mainwindow, text="subimt", command=makelist).grid(row=6, column=2)


def sherchoutput(info):
    results = Tk()
    Label(results, text="\n".join(info)).grid(row=1, column=1)
    Label(results, text="\n".join(info.values())).grid(row=1, column=2)


def sherch():
    tedt = sherchby.get()
    if tedt == "student":
        file = "role.csv"
    if tedt == "location":
        file = "stuff.csv"
    with open(file) as mainfile:
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
                print(info)
                sherchoutput(info)


def write():
    with open(writeas, "a") as mainfile:
        writer = csv.writer(mainfile)
        if writeas == 'stuff.csv':
            writer.writerows(reportdata)
        if writeas == "role.csv":
            writer.writerow(newstudent)


start()
startwindow.mainloop()
