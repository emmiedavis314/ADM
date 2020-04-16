# Class that contains the GUI for the game

#import
import sys
from tkinter import *
from tkinter.ttk import *
from beginning import *
#root that creates the main window, has to be first



class Menu():
    m = globals()['Begin']
    s_bar = 100
    h_bar = 100
    g_bar = 100
    functionName = "Hello"

    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        title = Label(self.master, text="Welcome to Aggie Decision Maker!")
        self.b1 = Button(self.master, text="Begin",command=lambda:[self.b1.pack_forget(), self.newWindow(), title.pack_forget()])
        foot = Label(self.master, text="Created for CSCE 445 @ TAMU by Natalie Burks, Emily Davis, Allison Reuthinger")
        foot.pack()
        foot.pack(side=BOTTOM)
        title.pack()
        self.b1.pack()
        self.frame.pack()

    def update_health(self, h, s, g):
        Menu.h_bar -= h
        Menu.s_bar -= s
        Menu.g_bar -= g
        #self.healthbars(Menu.h_bar, Menu.s_bar, Menu.g_bar)
        #self.newWindow()

    def healthbars(self, s_bar, g_bar, h_bar):
        progress = Frame(self.frame)
        he = Frame(progress)
        so = Frame(progress)
        gp = Frame(progress)
        h = Progressbar(he, orient=HORIZONTAL, length=s_bar, mode='determinate')
        s = Progressbar(so, orient=HORIZONTAL, length=g_bar, mode='determinate')
        g = Progressbar(gp, orient=HORIZONTAL, length=h_bar, mode='determinate')
        h['value'] = Menu.h_bar
        s['value'] = Menu.s_bar
        g['value'] = Menu.g_bar
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

    def newWindow(self):
        self.frame = Frame(self.master)
        title = Label(self.frame, text='Question 1')
        title.pack()
        self.healthbars(Menu.s_bar, Menu.g_bar, Menu.h_bar)
        self.frame.pack()
        Begin.bQuest1(self)

    def newWindow2(self, functionName, Q):
        self.frame = Frame(self.master)
        title = Label(self.frame, text=Q)
        title.pack()
        self.healthbars(Menu.s_bar, Menu.g_bar, Menu.h_bar)
        self.frame.pack()
        func = getattr(Menu.m, functionName)(self)

class mainGame():

    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.b3 = Button(self.master,text="text")



    #create widgets

    #header()
    #healthbars(100, 70, 50)
    #footer()
    #MainWindow.mainloop()