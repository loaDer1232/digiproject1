import csv
from tkinter import *
mainwindow = Tk()
entry = Entry(mainwindow).grid()
entry2 = Entry(mainwindow).grid()

def creader(): 
    file = open("stuff.csv")
    cav = csv.DictReader(file)
    print(cav)
    file.close()

def cwriter():
    file = open("stuff.csv")
    cav = csv.writer(file)
    file.close()

def main():
    Label(mainwindow, text="helllo world").grid()
    Label(mainwindow, text="hello2world").grid()
main()
