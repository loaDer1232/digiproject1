import ast
import csv
import time
from tkinter import *

startwindow = Tk()

dropvalues = ["student", "location", "day"]

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
    global sherchby
    sherchby = StringVar(mainwindow)
    sherchby.set("Select an Option")
    fuck = OptionMenu(mainwindow, sherchby, *dropvalues)
    fuck.grid(row=1, column=2)
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
        newstudent = [studentbox1.get(), studentbox2.get(), studentbox3.get()] #makes it so that i dont need to decaler every box a global varible and save mermoery somehow 
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
            reportbox5.get(),
            str(time.strftime("%x"))] #adds the date that the report was filled according to the system to prevent back dating
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
    if sherchby.get() == "student":
        file = "role.csv"
    elif sherchby.get() == "location" or "day":
        file = "stuff.csv"
    with open(file) as mainfile:
        csv.reader(mainfile)
        feilds = ast.literal_eval(str(next(mainfile).split(","))) #takes the values and makes a "list of lists"
        for i in mainfile:
            rows.append(i)
    for i in rows:
        print(i)
        data.append(dict(zip(feilds, str(i).split(",")))) #ties each value to its label to make them into sherchbale dictonarys

    Check = sherchbox.get()
    info = {}
    for i in data:
        if Check in i.values():
            if info != i: #this checks if the answer was found pervoslay and stops duplaction
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
