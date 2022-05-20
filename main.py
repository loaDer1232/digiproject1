import ast
import csv
import time
from tkinter import *

startwindow = Tk()

dropvalues = ["Student", "Location", "Day", "Date"]
classlist = ["A", "B", "C"]
typesofweather = ["Sunny", "Cloudy", "Windy", "Rainy", "Stormy"]

feilds = []
rows = []
data = []
info = {}


def start():
    Label(startwindow, text="Select Function",
          font=("bold", 13)).grid(row=1, column=1)
    Button(startwindow, text="Daily Report", command=daliyreportwindow,
           width=10, height=1).grid(row=2, column=1)
    Button(startwindow, text="Sherch", command=main,
           width=10, height=1).grid(row=2, column=2)
    Button(startwindow, text="Add Student", command=addstudentwindow,
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
    Label(mainwindow, text="Sherch By").grid(row=1, column=1)
    Label(mainwindow, text="Sherch For").grid(row=2, column=1)
    Button(mainwindow, text="Submit", command=rer,
           width=10, height=1).grid(row=3, column=2)
    global sherchbox
    sherchbox = Entry(mainwindow)
    sherchbox.grid(row=2, column=2)


def addstudentwindow():
    def makelist():
        Label(mainwindow, text="Submission Successful",
              foreground="green").grid(row=4, column=1)
        global newstudent
        # makes it so that i dont need to decaler every box a global varible and save mermoery somehow
        newstudent = [studentbox1.get().capitalize(), studentbox2.get().capitalize(),
                      studentbox3.get(), studentbox4.get()]
        write()
        mainwindow.destroy()
        addstudentwindow()
    mainwindow = Tk()
    global writeas
    writeas = "role.csv"
    Label(mainwindow, text="Student Last Name").grid(row=1, column=1)
    studentbox1 = Entry(mainwindow)
    studentbox1.grid(row=1, column=2)
    Label(mainwindow, text="Student First Name").grid(row=2, column=1)
    studentbox2 = Entry(mainwindow)
    studentbox2.grid(row=2, column=2)
    Label(mainwindow, text="Student Age").grid(row=3, column=1)
    studentbox3 = Spinbox(mainwindow, from_=14, to=18, wrap=True)
    studentbox3.grid(row=3, column=2)
    Label(mainwindow, text="Student Class").grid(row=4, column=1)
    studentbox4 = StringVar(mainwindow)
    studentbox4.set(classlist[0])
    clas = OptionMenu(mainwindow, studentbox4, *classlist)
    clas.grid(row=4, column=2)
    Button(mainwindow, text="Submit", command=makelist,
           width=10, height=1).grid(row=5, column=2)


def daliyreportwindow():
    def makelist():
        Label(mainwindow, text="Submission Successful",
              foreground="green").grid(row=6, column=1)
        global reportdata
        reportdata = [
            reportbox1.get().capitalize(),
            reportbox2.get(),
            reportbox3.get(),
            reportbox4.get(),
            reportbox5.get(),
            str(time.strftime("%x"))]  # adds the date that the report was filled according to the system to prevent back dating
        write()
        mainwindow.destroy()
        daliyreportwindow()
    mainwindow = Tk()
    global writeas
    writeas = "stuff.csv"
    Label(mainwindow, text="Location").grid(row=1, column=1)
    reportbox1 = Entry(mainwindow)
    reportbox1.grid(row=1, column=2)
    Label(mainwindow, text="Number of Students").grid(row=2, column=1)
    reportbox2 = Spinbox(mainwindow, from_=4, to=10, wrap=True)
    reportbox2.grid(row=2, column=2)
    Label(mainwindow, text="Day").grid(row=3, column=1)
    reportbox3 = Spinbox(mainwindow, from_=1, to=10, wrap=True)
    reportbox3.grid(row=3, column=2)
    Label(mainwindow, text="Weather").grid(row=4, column=1)
    reportbox4 = StringVar(mainwindow)
    reportbox4.set(typesofweather[0])
    weather = OptionMenu(mainwindow, reportbox4, *typesofweather)
    weather.grid(row=4, column=2)
    Label(mainwindow, text="Class").grid(row=5, column=1)
    reportbox5 = StringVar(mainwindow)
    reportbox5.set(classlist[0])
    clas = OptionMenu(mainwindow, reportbox5, *classlist)
    clas.grid(row=5, column=2)
    Button(mainwindow, text="Submit", command=makelist,
           width=10, height=1).grid(row=6, column=2)


def sherchoutput(info):
    results = Tk()
    Label(results, text="Results", font=("bold", 13)).grid(row=1, column=1)
    Label(results, text="\n".join(info)).grid(row=2, column=1)
    Label(results, text="\n".join(info.values())).grid(row=2, column=2)
    Button(results, text="Expaned", command=showmore).grid(row=3, column=2)


def showmore():
    if toopen == dropvalues[0]:
        toopen = dropvalues[1]
    elif toopen == dropvalues[1 or 2 or 3]:
        toopen = dropvalues[0]
    sherch()


def sherch():
    if toopen == dropvalues[0]:
        file = "role.csv"
    elif toopen == dropvalues[1 or 2 or 3]:
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

    Check = sherchbox.get().capitalize()
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