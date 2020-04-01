# Class that contains the GUI for the game

#import
from tkinter import *
from tkinter.ttk import *

#root that creates the main window, has to be first

MainWindow = Tk()

#define functions
def header():
    h = Frame(MainWindow)
    title = Label(h, text="Welcome to Aggie Decision Maker!")
    title.pack()
    subtitle = Label(h, text="This is the subtitle")
    subtitle.pack()
    button = Button(h, text="Test")
    button.pack()
    h.pack()

def healthbars(health, gpa, social):
    progress = Frame(MainWindow)
    he = Frame(progress)
    so = Frame(progress)
    gp = Frame(progress)
    h = Progressbar(he, orient=HORIZONTAL, length=100, mode='determinate')
    s = Progressbar(so, orient=HORIZONTAL, length=100, mode='determinate')
    g = Progressbar(gp, orient=HORIZONTAL, length=100, mode='determinate')
    h['value'] = health
    s['value'] = gpa
    g['value'] = social
    h_text = Label(he, text="Health: ")
    h_text.pack(side=LEFT)
    s_text = Label(so, text="Social:  ")
    s_text.pack(side=LEFT)
    g_text = Label(gp, text="GPA:     ")
    g_text.pack(side=LEFT)
    h.pack(side=RIGHT)
    s.pack(side=RIGHT)
    g.pack(side=RIGHT)
    he.pack()
    so.pack()
    gp.pack()
    progress.pack()


def footer():
    b = Frame(MainWindow)
    foot = Label(b, text="Created for CSCE 445 @ TAMU by Natalie Burks, Emily Davis, Allison Reuthinger")
    foot.pack()
    b.pack(side=BOTTOM)

#create widgets

header()
healthbars(100, 70, 50)
footer()
MainWindow.mainloop()