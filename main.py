import ast
import csv
from tkinter import *

startwindow = Tk()

dropvalues = ["student", "location", "day"]
sherchby = StringVar()


feilds = []
rows = []
data = []
info = {}


def start():
    Label(startwindow, text="selcet function",
          font=("bold", 13)).grid(row=1, column=1)
    Button(startwindow, text="daily report", command=daliyreportwindow,
           width=10, height=1).grid(row=2, column=1)
    Button(startwindow, text="sherch", command=main,
           width=10, height=1).grid(row=2, column=2)
    Button(startwindow, text="add student", command=addstudentwindow,
           width=10, height=1).grid(row=3, column=1)
    Button(startwindow, text="Quit", command=exit,
           width=10, height=1).grid(row=3, column=2)


def main():
    mainwindow = Tk()
    OptionMenu(mainwindow, sherchby, *dropvalues).grid(row=1, column=2)
    Label(mainwindow, text="sherch by").grid(row=1, column=1)
    Label(mainwindow, text="sherch for").grid(row=2, column=1)
    Button(mainwindow, text="submit", command=sherch,
           width=10, height=1).grid(row=3, column=2)
    global sherchbox
    sherchbox = Entry(mainwindow)
    sherchbox.grid(row=2, column=2)


def addstudentwindow():
    def makelist():
        Label(mainwindow, text="subitisoin sucseful",
              foreground="green").grid(row=4, column=1)
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
    Button(mainwindow, text="subimt", command=makelist,
           width=10, height=1).grid(row=4, column=2)


def daliyreportwindow():
    def makelist():
        Label(mainwindow, text="subitisoin sucseful",
              foreground="green").grid(row=6, column=1)
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
    Button(mainwindow, text="subimt", command=makelist,
           width=10, height=1).grid(row=6, column=2)


def sherchoutput(info):
    results = Tk()
    Label(results, text="results", font=("bold", 13)).grid(row=1, column=1)
    Label(results, text="\n".join(info)).grid(row=2, column=1)
    Label(results, text="\n".join(info.values())).grid(row=2, column=2)


def sherch():
    tedt = sherchby.get()
    if tedt == "student":
        file = "role.csv"
    if tedt == "location" or "day":
        file = "stuff.csv"
    with open(file) as mainfile:
        csv.reader(mainfile)
        feilds = ast.literal_eval(str(next(mainfile).split(",")))
        for i in mainfile:
            rows.append(i)
    for i in rows:
        print(i)
        data.append(dict(zip(feilds, str(i).split(","))))

    Check = sherchbox.get()
    for i in data:
        for e in i.values():
            if Check in e:
                info = i
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
