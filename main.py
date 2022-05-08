import ast
import csv
import time
from tkinter import *

startwindow = Tk()

dropvalues = ["student", "location", "day", "date"]
classlist = ["A", "B", "C"]
typesofweather = ["sunny", "cloudy", "windy", "rainy", "stormy"]

feilds = []
rows = []
data = []
info = {}


def start():
    Label(startwindow, text="select function",
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
    def rer():
        global toopen
        toopen = sherchby.get()
        sherch()
    mainwindow = Tk()
    sherchby = StringVar(mainwindow)
    sherchby.set("Select an Option")
    fuck = OptionMenu(mainwindow, sherchby, *dropvalues)
    fuck.grid(row=1, column=2)
    Label(mainwindow, text="sherch by").grid(row=1, column=1)
    Label(mainwindow, text="sherch for").grid(row=2, column=1)
    Button(mainwindow, text="submit", command=rer,
           width=10, height=1).grid(row=3, column=2)
    global sherchbox
    sherchbox = Entry(mainwindow)
    sherchbox.grid(row=2, column=2)


def addstudentwindow():
    def makelist():
        Label(mainwindow, text="submission successful",
              foreground="green").grid(row=4, column=1)
        global newstudent
        # makes it so that i dont need to decaler every box a global varible and save mermoery somehow
        newstudent = [studentbox1.get(), studentbox2.get(),
                      studentbox3.get(), studentbox4.get()]
        write()
    mainwindow = Tk()
    global writeas
    writeas = "role.csv"
    Label(mainwindow, text="student last name").grid(row=1, column=1)
    studentbox1 = Entry(mainwindow)
    studentbox1.grid(row=1, column=2)
    Label(mainwindow, text="student first name").grid(row=2, column=1)
    studentbox2 = Entry(mainwindow)
    studentbox2.grid(row=2, column=2)
    Label(mainwindow, text="student age").grid(row=3, column=1)
    studentbox3 = Spinbox(mainwindow, from_=14, to=18, wrap=True)
    studentbox3.grid(row=3, column=2)
    Label(mainwindow, text="student class").grid(row=4, column=1)
    studentbox4 = StringVar(mainwindow)
    studentbox4.set(classlist[0])
    clas = OptionMenu(mainwindow, studentbox4, *classlist)
    clas.grid(row=4, column=2)
    Button(mainwindow, text="submit", command=makelist,
           width=10, height=1).grid(row=5, column=2)


def daliyreportwindow():
    def makelist():
        Label(mainwindow, text="submission successful",
              foreground="green").grid(row=6, column=1)
        global reportdata
        reportdata = [
            reportbox1.get(),
            reportbox2.get(),
            reportbox3.get(),
            reportbox4.get(),
            reportbox5.get(),
            str(time.strftime("%x"))]  # adds the date that the report was filled according to the system to prevent back dating
        write()
    mainwindow = Tk()
    global writeas
    writeas = "stuff.csv"
    Label(mainwindow, text="location").grid(row=1, column=1)
    reportbox1 = Entry(mainwindow)
    reportbox1.grid(row=1, column=2)
    Label(mainwindow, text="number of students").grid(row=2, column=1)
    reportbox2 = Spinbox(mainwindow, from_=4, to=10, wrap=True)
    reportbox2.grid(row=2, column=2)
    Label(mainwindow, text="day").grid(row=3, column=1)
    reportbox3 = Spinbox(mainwindow, from_=1, to=10, wrap=True)
    reportbox3.grid(row=3, column=2)
    Label(mainwindow, text="weather").grid(row=4, column=1)
    reportbox4 = StringVar(mainwindow)
    reportbox4.set(typesofweather[0])
    weather = OptionMenu(mainwindow, reportbox4, *typesofweather)
    weather.grid(row=4, column=2)
    Label(mainwindow, text="class").grid(row=5, column=1)
    reportbox5 = StringVar(mainwindow)
    reportbox5.set(classlist[0])
    clas = OptionMenu(mainwindow, reportbox5, *classlist)
    clas.grid(row=5, column=2)
    Button(mainwindow, text="submit", command=makelist,
           width=10, height=1).grid(row=6, column=2)


def sherchoutput(info):
    results = Tk()
    Label(results, text="results", font=("bold", 13)).grid(row=1, column=1)
    Label(results, text="\n".join(info)).grid(row=2, column=1)
    Label(results, text="\n".join(info.values())).grid(row=2, column=2)
    Button(results, text="expaned", command=showmore).grid(row=3, column=2)


def showmore():
    if toopen == "student":
        toopen = "stuff.csv"
    elif toopen == "location" or "day":
        toopen = "role.csv"
    sherch()


def sherch():
    if toopen == "student":
        file = "role.csv"
    elif toopen == "location" or "day" or "date":
        file = "stuff.csv"
    with open(file) as mainfile:
        csv.reader(mainfile)
        # takes the values and makes a "list of lists"
        feilds = ast.literal_eval(str(next(mainfile).split(",")))
        for i in mainfile:
            rows.append(i)
    for i in rows:
        print(i)
        # ties each value to its label to make them into sherchbale dictonarys
        data.append(dict(zip(feilds, str(i).split(","))))

    Check = sherchbox.get()
    info = {}
    for i in data:
        if Check in i.values():
            if info != i:  # this checks if the answer was found pervoslay and stops duplaction
                info = i
                sherchoutput(info)


def write():
    with open(writeas, "a") as mainfile:
        writer = csv.writer(mainfile)
        if writeas == 'stuff.csv':
            writer.writerow(reportdata)
        if writeas == "role.csv":
            writer.writerow(newstudent)


start()
startwindow.mainloop()
