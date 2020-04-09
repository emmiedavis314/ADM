# Class that contains the GUI for the game

#import
from tkinter import *
from tkinter.ttk import *
from beginning import *
#root that creates the main window, has to be first
'''
class GUI(): 

    #MainWindow = Tk()
    #MainWindow.geometry("500x500")

    #define functions
    def mainGame(self):
        main = Tk()
        main.geometry("500x500")
        title = Label(main, text="Welcome to Aggie Decision Maker!")
        title.pack()
        subtitle = Label(main, text="This is the subtitle")
        subtitle.pack()
        button = Button(main, text="Test")
        button.pack()
        

    def menu(self):
        m = Tk()
        m.geometry("500x500")
        title = Label(m , text="Welcome to Aggie Decision Maker!")
        title.pack()
        self.button = Button(m, text="Begin", command=GUI.mainGame(self))
        self.button.pack()
        m.pack()
 '''
        
'''

    def footer(self):
        b = Frame(GUI.MainWindow)
        foot = Label(b, text="Created for CSCE 445 @ TAMU by Natalie Burks, Emily Davis, Allison Reuthinger")
        foot.pack()
        b.pack(side=BOTTOM)
        
'''


class Menu():

    s_bar = 100
    h_bar = 100
    g_bar = 100


    def __init__(self,master):
        self.master = master
        self.frame = Frame(self.master)
        title = Label(self.master , text="Welcome to Aggie Decision Maker!")
        self.b1 = Button(self.master, text="Begin",command=lambda:[self.b1.pack_forget(), self.newWindow()])
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

    def healthbars(self):
        progress = Frame(self.frame)
        he = Frame(progress)
        so = Frame(progress)
        gp = Frame(progress)
        h = Progressbar(he, orient=HORIZONTAL, length=100, mode='determinate')
        s = Progressbar(so, orient=HORIZONTAL, length=100, mode='determinate')
        g = Progressbar(gp, orient=HORIZONTAL, length=100, mode='determinate')
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
        self.healthbars()
        self.frame.pack()
        title = Label(self.master, text='Question 1')
        title.pack()
        Begin.bQuest1(self)

class mainGame():

    def __init__(self,master):
        self.master = master
        self.frame = Frame(self.master)   
        self.b3 = Button(self.master,text="text")         



    #create widgets

    #header()
    #healthbars(100, 70, 50)
    #footer()
    #MainWindow.mainloop()