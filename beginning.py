# Class that contains the beginning portion of the game
from Menu import *
from tkinter import *
from tkinter.ttk import *

class Begin(Menu):

    def bQuest1(self):
        question_description = "It’s your first day of school in Aggieland! " \
                               "You have already become best friends with your suitemates, " \
                               "and they invited you to lunch today. But, you have a class during " \
                               "lunch. Do you:"
        option_h = "Skip lunch but stay home and sleep."
        option_s = "Suggest Chick-Fil-A at the MSC for lunch!"
        option_g = "Skip lunch and go to class."
        question = Label(self.frame, text=question_description)
        h = Button(self.frame, text=option_h, command=lambda:[Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(0, 5, 5)])
        s = Button(self.frame, text=option_s, command=lambda:[Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 0, 5)])
        g = Button(self.frame, text=option_g, command=lambda:[Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 5, 0)])
        question.pack()
        h.pack()
        s.pack()
        g.pack()


    def bQuest2(self):
        self.healthbars()
        question_description = Label(self.master, text="this is question2")
        #option_h = "health"
        #option_s = "social"
        #option_g = "gpa"
        question_description.pack()
        #option_h.pack()
        #option_s.pack()
        #option_g.pack()

    def bQuest3(self):
        pass

    def bQuest4(self):
        pass

    def bQuest5(self):   
        pass         