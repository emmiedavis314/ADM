# Class that contains the GUI for the game

# import
import sys
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *

import tkinter as tk

from beginning import *
from tkinter import font as tkFont

# root that creates the main window, has to be first


class Menu():
    m = globals()['Begin']
    s_bar = 100
    h_bar = 100
    g_bar = 100
    functionName = "Hello"
    gameOver = False

    def reset(self):
        Menu.gameOver = False

    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        title = tkinter.Label(self.master, text = 'Welcome to Aggie Decision Maker!', font = ('Helvetica',30), bg = '#500000', fg = 'white')
        self.b1 = tkinter.Button(self.master, text="Begin", font=('Helvetica'),
                         command=lambda: [self.b1.pack_forget(), self.newWindow(), title.pack_forget()])
        foot = tkinter.Label(self.master, text="Created for CSCE 445 @ TAMU by Natalie Burks, Emily Davis, Allison Reuthinger", font = ('Helvetica'), bg = '#500000', fg = 'white')
        foot.pack()
        foot.pack(side=BOTTOM, pady=10)
        title.pack(pady=15, padx=20)
        self.b1.pack(pady=15, fill="none", expand=True, ipady=5, ipadx=10)
        self.frame.pack(pady=30,)

    def update_health(self, h, s, g):
        if (h == 100) and (s == 100) and (g == 100):
            Menu.h_bar = 100
            Menu.s_bar = 100
            Menu.g_bar = 100
        else:
            if Menu.h_bar - h <= 100:
                Menu.h_bar -= h
                if Menu.h_bar <= 0:
                    self.newWindow2('game_over', 'You lose! Health at 0.')
                    return
            if Menu.s_bar - s <= 100:
                Menu.s_bar -= s
                if Menu.s_bar <= 0:
                    self.newWindow2('game_over', 'You lose! Social at 0.')
                    return
            if Menu.g_bar - g <= 100:
                Menu.g_bar -= g
                if Menu.g_bar <= 0:
                    self.newWindow2('game_over', 'You lose! GPA at 0.')
                    return
        # self.healthbars(Menu.h_bar, Menu.s_bar, Menu.g_bar)
        # self.newWindow()

    def healthbars(self, s_bar, g_bar, h_bar):
        progress = tk.Frame(self.frame, bg='white')
        he = tk.Frame(progress, bg='white')
        so = tk.Frame(progress, bg='white')
        gp = tk.Frame(progress, bg='white')
        hStyle = ttk.Style()
        hStyle.theme_use('alt')
        sStyle = ttk.Style()
        sStyle.theme_use('alt')
        gStyle = ttk.Style()
        gStyle.theme_use('alt')
    # health status bar
        if(h_bar >= 80):
            hStyle.configure("green.Horizontal.TProgressbar", background='green')
            h = Progressbar(he, orient=HORIZONTAL, length=100, mode='determinate', style="green.Horizontal.TProgressbar")
        elif(h_bar >=70 and h_bar <= 79 ):
            hStyle.configure("yellow.Horizontal.TProgressbar", background='yellow')
            h = Progressbar(he, orient=HORIZONTAL, length=100, mode='determinate', style="yellow.Horizontal.TProgressbar")
        elif(h_bar <= 69):
            hStyle.configure("red.Horizontal.TProgressbar", background='red')
            h = Progressbar(he, orient=HORIZONTAL, length=100, mode='determinate', style="red.Horizontal.TProgressbar")
     # social status bar
        if(s_bar >= 80):
            sStyle.configure("green.Horizontal.TProgressbar", background='green')
            s = Progressbar(so, orient=HORIZONTAL, length=100, mode='determinate', style="green.Horizontal.TProgressbar")
        elif(s_bar >=70 and s_bar <= 79 ):
            sStyle.configure("yellow.Horizontal.TProgressbar", background='yellow')
            s = Progressbar(so, orient=HORIZONTAL, length=100, mode='determinate', style="yellow.Horizontal.TProgressbar")
        elif(s_bar <= 69):
            sStyle.configure("red.Horizontal.TProgressbar", background='red')
            s = Progressbar(so, orient=HORIZONTAL, length=100, mode='determinate', style="red.Horizontal.TProgressbar")
    # gpa status bar
        if (g_bar >= 80):
            gStyle.configure("green.Horizontal.TProgressbar", background='green')
            g = Progressbar(gp, orient=HORIZONTAL, length=100, mode='determinate',
                            style="green.Horizontal.TProgressbar")
        elif (g_bar >= 70 and g_bar <= 79):
            gStyle.configure("yellow.Horizontal.TProgressbar", background='yellow')
            g = Progressbar(gp, orient=HORIZONTAL, length=100, mode='determinate',
                            style="yellow.Horizontal.TProgressbar")
        elif(g_bar <= 69):
            gStyle.configure("red.Horizontal.TProgressbar", background='red')
            g = Progressbar(gp, orient=HORIZONTAL, length=100, mode='determinate', style="red.Horizontal.TProgressbar")

        h['value'] = Menu.h_bar
        s['value'] = Menu.s_bar
        g['value'] = Menu.g_bar
        h_text = tkinter.Label(he, text="Health: ")
        h_text.pack(side=LEFT)
        s_text = tkinter.Label(so, text="Social:  ")
        s_text.pack(side=LEFT)
        g_text = tkinter.Label(gp, text="GPA:     ")
        g_text.pack(side=LEFT)
        h.pack(side=RIGHT)
        s.pack(side=RIGHT)
        g.pack(side=RIGHT)
        he.pack()
        so.pack()
        gp.pack()
        progress.pack()

    def newWindow(self):
        self.frame = tk.Frame(self.master, bg='white')
        title = tkinter.Label(self.frame, text='Question 1', font = ('Helvetica'))
        title.pack()
        self.healthbars(Menu.s_bar, Menu.g_bar, Menu.h_bar)
        self.frame.pack(ipady=20, ipadx=20)
        Begin.bQuest1(self)

    def newWindow2(self, functionName, Q):
        if functionName != 'game_over' and Menu.gameOver is False:
            self.frame = tk.Frame(self.master, bg='white')
            title = tkinter.Label(self.frame, text=Q, font = ('Helvetica'))
            title.pack()
            self.healthbars(Menu.s_bar, Menu.g_bar, Menu.h_bar)
            self.frame.pack(ipady=20, ipadx=20)
            func = getattr(Menu.m, functionName)(self)
        elif functionName == 'game_over':
            Menu.gameOver = True
            self.frame = tk.Frame(self.master, bg='white')
            title = tkinter.Label(self.frame, text=Q, font = ('Helvetica', 20))
            title.pack()
            self.healthbars(Menu.s_bar, Menu.g_bar, Menu.h_bar)
            self.frame.pack(ipady=20, ipadx=20)
            func = getattr(Menu.m, functionName)(self)

    def popup1(self):
        popup = Tk()
        popup['bg'] = '#500000'
        popup.geometry('600x150')
        popup.wm_title("Random Event")
        label = tkinter.Label(popup, text="Unfortunately you waited too long to start the project and had some unforeseen "
                                      "difficulties. Because of this, you had to turn in the project late.", wraplength=500, bg='#500000', fg='white', font=('Helvetica'))
        label.pack(side="top", fill="x", pady=20, padx=20)
        B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
        Menu.g_bar -= 10
        B1.pack()
        popup.mainloop()

    def popup2(self):
        popup = Tk()
        popup['bg'] = '#500000'
        popup.geometry('600x150')
        popup.wm_title("Random Event")
        label = tkinter.Label(popup, text="Oh no! The party got a little crazy and the cops were called. No big deal, "
                                      "but you aren't the angel that your parents think you are. Looks like you are "
                                      "spending the weekend in jail.", wraplength=500, bg='#500000', fg='white', font=('Helvetica'))
        label.pack(side="top", fill="x", pady=20, padx=20)
        B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
        Menu.s_bar -= 10
        B1.pack()
        popup.mainloop()

    def popup3(self):
        popup = Tk()
        popup['bg'] = '#500000'
        popup.geometry('600x150')
        popup.wm_title("Random Event")
        label = tkinter.Label(popup, text="So you decide to go to your brother's football game. However, in all of the "
                                      "excitement you forgot to turn in your homework. Ouch, that's going to hurt "
                                      "your grade.", wraplength=500, bg='#500000', fg='white', font=('Helvetica'))
        label.pack(side="top", fill="x", pady=20, padx=20)
        B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
        Menu.g_bar -= 10
        B1.pack()
        popup.mainloop()

    def popup4(self):
        popup = Tk()
        popup['bg'] = '#500000'
        popup.geometry('600x150')
        popup.wm_title("Random Event")
        label = tkinter.Label(popup, text="Congraulations!!! All of that hardwork paid off and you won the weightllifting "
                                      "competition.", wraplength=500, bg='#500000', fg='white', font=('Helvetica'))
        label.pack(side="top", fill="x", pady=20, padx=20)
        B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
        Menu.h_bar += 10
        B1.pack()
        popup.mainloop()

    def popup5(self):
        popup = Tk()
        popup['bg'] = '#500000'
        popup.geometry('600x150')
        popup.wm_title("Random Event")
        label = tkinter.Label(popup, text="Unfortunately you not putting in the extra practice caused you to not only not "
                                      "even place in the weightlifting competition, but caused to only make 2/6 "
                                      "lifts.", wraplength=500, bg='#500000', fg='white', font=('Helvetica'))
        label.pack(side="top", fill="x", pady=20, padx=20)
        B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
        Menu.h_bar -= 10
        B1.pack()
        popup.mainloop()

    def popup6(self):
        popup = Tk()
        popup['bg'] = '#500000'
        popup.geometry('600x150')
        popup.wm_title("Random Event")
        label = tkinter.Label(popup, text="You had this amazing idea to finish the project on the plane ride home. "
                                      "However, the WiFi was not working and you couldn't finish. You had to beg the "
                                      "professor to let you turn in the project with a 40% deduction on the "
                                      "assignment. Not only did this hurt your grade, but also your pride.", wraplength=500, bg='#500000', fg='white', font=('Helvetica'))
        label.pack(side="top", fill="x", pady=20, padx=20)
        B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
        Menu.g_bar -= 10
        Menu.h_bar -= 5
        B1.pack()
        popup.mainloop()

    def popup7(self):
        popup = Tk()
        popup['bg'] = '#500000'
        popup.geometry('600x150')
        popup.wm_title("Random Event")
        label = tkinter.Label(popup, text="The event was during one of your classes and you missed an attendance " \
                                      "grade. It would’ve been worth it, but the companies just told you to apply "
                                      "online " \
                                      "and it’s unlikely you will get a callback because they don’t hire freshmen.", wraplength=500, bg='#500000', fg='white', font=('Helvetica'))
        label.pack(side="top", fill="x", pady=20, padx=20)
        B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
        Menu.g_bar -= 10
        B1.pack()
        popup.mainloop()

    def popup8(self):
        popup = Tk()
        popup['bg'] = '#500000'
        popup.geometry('600x150')
        popup.wm_title("Random Event")
        label = tkinter.Label(popup, text="Luckily, you impressed a small company in your hometown with your tenacity to "
                                      "learn new things. They decided to give you a chance and they gave you an "
                                      "internship for the summer.", wraplength=500, bg='#500000', fg='white', font=('Helvetica'))
        label.pack(side="top", fill="x", pady=20, padx=20)
        B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
        Menu.s_bar += 10
        B1.pack()
        popup.mainloop()

    def popup9(self):
        popup = Tk()
        popup['bg'] = '#500000'
        popup.geometry('600x150')
        popup.wm_title("Random Event")
        label = tkinter.Label(popup, text="You get sick because you haven’t " \
                                      "been eating well or getting enough sleep, and therefore have to turn your " \
                                      "paper in late. ", wraplength=500, bg='#500000', fg='white', font=('Helvetica'))
        label.pack(side="top", fill="x", pady=20, padx=20)
        B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
        Menu.h_bar -= 10
        B1.pack()
        popup.mainloop()

    def popup10(self):
        popup = Tk()
        popup['bg'] = '#500000'
        popup.geometry('600x150')
        popup.wm_title("Random Event")
        label = tkinter.Label(popup, text="Your friend's battery dies and has to stay a few " \
                                      "extra days, so you have to cram for the test on Monday morning.", wraplength=500, bg='#500000', fg='white', font=('Helvetica'))
        label.pack(side="top", fill="x", pady=20, padx=20)
        B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
        Menu.s_bar += 5
        Menu.g_bar -= 5
        B1.pack()
        popup.mainloop()

    def popup11(self):
        popup = Tk()
        popup['bg'] = '#500000'
        popup.geometry('600x150')
        popup.wm_title("Random Event")
        label = tkinter.Label(popup, text="Pop quiz! Good thing you were present. Professor KillJoy’s " \
                                      "random question about the color of his shirt earned you 10 bonus points " \
                                      "on the next test.)", wraplength=500, bg='#500000', fg='white', font=('Helvetica'))
        label.pack(side="top", fill="x", pady=20, padx=20)
        B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
        Menu.g_bar += 10
        B1.pack()
        popup.mainloop()

    def popup12(self):
        popup = Tk()
        popup['bg'] = '#500000'
        popup.geometry('600x150')
        popup.wm_title("Random Event")
        label = tkinter.Label(popup, text="In all your efforts to " \
                                      "not oversleep by staying up all night, you fall asleep 5 minutes before your" \
                                      "registration time, and some of your classes fill up.", wraplength=500, bg='#500000', fg='white', font=('Helvetica'))
        label.pack(side="top", fill="x", pady=20, padx=20)
        B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
        Menu.h_bar -= 10
        Menu.g_bar -= 3
        B1.pack()
        popup.mainloop()


class mainGame():

    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master, bg='white')
        self.b3 = tkinter.Button(self.master, text="text", bg='white')

    # create widgets

    # header()
    # healthbars(100, 70, 50)
    # footer()
    # MainWindow.mainloop()
