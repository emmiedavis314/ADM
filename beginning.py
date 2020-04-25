# Class that contains the beginning portion of the game
from Gui import *
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
        h = Button(self.frame, text=option_h, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(0, 5, 5), self.newWindow2('bQuest2', 'question2')])
        s = Button(self.frame, text=option_s, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 0, 5), self.newWindow2('bQuest2', 'question2')])
        g = Button(self.frame, text=option_g, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 5, 0), self.newWindow2('bQuest2', 'question2')])
        question.pack()
        h.pack()
        s.pack()
        g.pack()


    def bQuest2(self):
        question_description = "Congratulations you have finished your 1st week at A&M! You have made some new " \
                               "friends and they have invited you to go to a party this weekend. However, you have a " \
                               "quiz coming up that you need to study for. Do you: "
        option_h = "Party it UPPPP!!! It’s College you are supposed to make mistakes."
        option_s = "Stay home and study."
        option_g = "Meal prep for the coming week."
        question = Label(self.frame, text=question_description)
        h = Button(self.frame, text=option_h, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(0, 5, 5), self.newWindow2('bQuest3', 'question3')])
        s = Button(self.frame, text=option_s, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 0, 5), self.newWindow2('bQuest3', 'question3')])
        g = Button(self.frame, text=option_g, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 5, 0), self.newWindow2('bQuest3', 'question3')])
        question.pack()
        h.pack()
        s.pack()
        g.pack()

    def bQuest3(self):

        question_description = "It’s the second week of school and your classes are starting to pick up. Your first " \
                               "programming assignment is not due until next week though. Do you: "
        option_h = "Procrastinate and play Animal Crossing with some friends, it’s not due until next week anyway.(If " \
                   "they choose this option then have a pop up stating that they had to turn the project in late) "
        option_s = "Start early, you have never coded before."
        option_g = "Go to the gym and get swole. I can start on it tomorrow."
        question = Label(self.frame, text=question_description)
        h = Button(self.frame, text=option_h, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(0, 5, 5), self.newWindow2('bQuest4', 'question 4')])
        s = Button(self.frame, text=option_s, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 0, 5), self.newWindow2('bQuest4', 'question 4')])
        g = Button(self.frame, text=option_g, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 5, 0), self.newWindow2('bQuest4', 'question 4')])
        question.pack()
        h.pack()
        s.pack()
        g.pack()

    def bQuest4(self):

        question_description = "The controversial Thursday night football game is tonight, and you have an 8 am class " \
                               "in the morning. Do you: "
        option_h = "Be the redass Aggie that you are and just go to the game. You’re really only here for football " \
                   "anyways. "
        option_s = "Be a supportive Ag and go to the game but also be up in time for class."
        option_g = "Who cares about football? You’ll be in class though."
        question = Label(self.frame, text=question_description)
        h = Button(self.frame, text=option_h, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(0, 5, 5), self.newWindow2('bQuest5', 'question 5')])
        s = Button(self.frame, text=option_s, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 0, 5), self.newWindow2('bQuest5', 'question 5')])
        g = Button(self.frame, text=option_g, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 5, 0), self.newWindow2('bQuest5', 'question 5')])
        question.pack()
        h.pack()
        s.pack()
        g.pack()

    def bQuest5(self):

        question_description = "Ahh mondays. You’re super tired after this weekend. Maybe you can sleep in and get " \
                               "breakfast instead of class? "
        option_h = "Definitely gonna sleep until noon and eat a “late breakfast"
        option_s = "Meet up with your suitemates for a breakfast date"
        option_g = "No way. What if they take attendance?"
        question = Label(self.frame, text=question_description)
        h = Button(self.frame, text=option_h, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(0, 5, 5), self.newWindow2('bQuest6', 'question 6')])
        s = Button(self.frame, text=option_s, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 0, 5), self.newWindow2('bQuest6', 'question 6')])
        g = Button(self.frame, text=option_g, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 5, 0), self.newWindow2('bQuest6', 'question 6')])
        question.pack()
        h.pack()
        s.pack()
        g.pack()

    def bQuest6(self):

        question_description = "There is a frat party this weekend and your new found college friends have invited " \
                               "you to come. Should you: "
        option_h = "Go and Have fun! This is your first college party. (random event: cops got called, and everyone " \
                   "underaged went to jail "
        option_s = "Start planning for the week to come."
        option_g = "Go for a run"
        question = Label(self.frame, text=question_description)
        h = Button(self.frame, text=option_h, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(0, 5, 5), self.newWindow2('bQuest7', 'question 7')])
        s = Button(self.frame, text=option_s, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 0, 5), self.newWindow2('bQuest7', 'question 7')])
        g = Button(self.frame, text=option_g, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 5, 0), self.newWindow2('bQuest7', 'question 7')])
        question.pack()
        h.pack()
        s.pack()
        g.pack()

    def bQuest7(self):

        question_description = "It’s Tuesday night, aka time for Breakaway! But, you have an exam tomorrow in CSCE " \
                               "222 that you just remembered about. Should you: "
        option_h = "Take the time off and go to Breakaway, and stay up until the early hours of the morning studying " \
                   "for your exam with your friends. "
        option_s = "Go to breakaway, but go straight to sleep afterwards. Can’t do well on an exam without sleep!"
        option_g = "Skip breakaway and study at Zachry."
        question = Label(self.frame, text=question_description)
        h = Button(self.frame, text=option_h, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(0, 5, 5), self.newWindow2('bQuest8', 'question 8')])
        s = Button(self.frame, text=option_s, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 0, 5), self.newWindow2('bQuest8', 'question 8')])
        g = Button(self.frame, text=option_g, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 5, 0), self.newWindow2('bQuest8', 'question 8')])
        question.pack()
        h.pack()
        s.pack()
        g.pack()

    def bQuest8(self):

        question_description = "Friday night is here, which means it’s time for the weekend! Your roomies have " \
                               "invited you to go out to The Chicken to celebrate! Do you: "
        option_h = "Go and spend some quality time with your friends over a plate of cheese fries!"
        option_s = "Stay at home and binge the new season of Stranger Things on Netflix. You had a long week!"
        option_g = "Offer to order cheese fries to go if your roomies will study with you in ZACH instead :)"
        question = Label(self.frame, text=question_description)
        h = Button(self.frame, text=option_h, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(0, 5, 5), self.newWindow2('bQuest9', 'question 9')])
        s = Button(self.frame, text=option_s, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 0, 5), self.newWindow2('bQuest9', 'question 9')])
        g = Button(self.frame, text=option_g, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 5, 0), self.newWindow2('bQuest9', 'question 9')])
        question.pack()
        h.pack()
        s.pack()
        g.pack()

    def bQuest9(self):

        question_description = "It’s the week you’ve been dreading: first exams. How do you prepare?"
        option_h = "Meal prep all your breakfasts and lunches! You won’t have time to think about meals with all that " \
                   "studying you’ll be doing. "
        option_s = "Total study overdrive. Red bull and Evans, here you come!"
        option_g = "You talk with your roomies and decide to keep each other accountable! You will make sure everyone " \
                   "takes care of themselves and studies hard. "
        question = Label(self.frame, text=question_description)
        h = Button(self.frame, text=option_h, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(0, 5, 5), self.newWindow2('bQuest10', 'question 10')])
        s = Button(self.frame, text=option_s, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 0, 5), self.newWindow2('bQuest10', 'question 10')])
        g = Button(self.frame, text=option_g, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 5, 0), self.newWindow2('bQuest10', 'question 10')])
        question.pack()
        h.pack()
        s.pack()
        g.pack()

    def bQuest10(self):

        question_description = "After that long week, you are really excited to drive home for the first time in " \
                               "forever! Your brother has a football game tonight, and your family has invited you " \
                               "out to support him. However, you put off a programming assignment (that’s due at " \
                               "midnight!!!) to study for all of your exams. Do you: "
        option_h = "Go to the game and cheer the loudest that you can! Family is more important than Homework.(popup " \
                   "with a more decrease to GPA) "
        option_s = "Tell your brother that you will congratulate him with ice cream when he is done, and head " \
                   "straight home to finish your assignment. "
        option_g = "Volunteer to help with warm ups! You can exercise and support your family."
        question = Label(self.frame, text=question_description)
        h = Button(self.frame, text=option_h, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(0, 5, 5), self.newWindow2('bQuest3', 'question3')])
        s = Button(self.frame, text=option_s, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 0, 5), self.newWindow2('bQuest3', 'question3')])
        g = Button(self.frame, text=option_g, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 5, 0), self.newWindow2('bQuest3', 'question3')])
        question.pack()
        h.pack()
        s.pack()
        g.pack()