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
        question = tkinter.Label(self.frame, text=question_description, wraplength=500, bg='white')
        h = tkinter.Button(self.frame, text=option_h, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(-5, 5, 5), self.newWindow2('bQuest2', 'Question 2')])
        s = tkinter.Button(self.frame, text=option_s, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, -5, 5), self.newWindow2('bQuest2', 'Question 2')])
        g = tkinter.Button(self.frame, text=option_g, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 5, -5), self.newWindow2('bQuest2', 'Question 2')])
        question.pack(padx=20, pady=15)
        h.pack(pady=5)
        s.pack(pady=5)
        g.pack(pady=5)


    def bQuest2(self):
        question_description = "Congratulations you have finished your 1st week at A&M! You have made some new " \
                               "friends and they have invited you to go to a party this weekend. However, you have a " \
                               "quiz coming up that you need to study for. Do you: "
        option_h = "Meal prep for the coming week."
        option_s = "Party it UPPPP!!! It’s college; you are supposed to make mistakes."
        option_g = "Stay home and study."
        question = tkinter.Label(self.frame, text=question_description, wraplength=500, bg='white')
        h = tkinter.Button(self.frame, text=option_h, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(-5, 5, 5), self.newWindow2('bQuest3', 'Question 3')])
        s = tkinter.Button(self.frame, text=option_s, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, -5, 5), self.newWindow2('bQuest3', 'Question 3')])
        g = tkinter.Button(self.frame, text=option_g, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 5, -5), self.newWindow2('bQuest3', 'Question 3')])
        question.pack(padx=20, pady=15)
        h.pack(pady=5)
        s.pack(pady=5)
        g.pack(pady=5)

    def bQuest3(self):

        question_description = "It’s the second week of school and your classes are starting to pick up. Your first " \
                               "programming assignment is not due until next week though. Do you: "
        option_h = "Go to the gym and get swole. I can start on it tomorrow."
        option_s = "Procrastinate and play Animal Crossing with some friends, it’s not due until next week anyway."
        option_g = "Start early, you have never coded before."
        question = tkinter.Label(self.frame, text=question_description, wraplength=500, bg='white')
        h = tkinter.Button(self.frame, text=option_h, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(-5, 5, 5), self.newWindow2('bQuest4', 'Question 4')])
        s = tkinter.Button(self.frame, text=option_s, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, -5, 5), self.newWindow2('bQuest4', 'Question 4'), self.popup1()])
        g = tkinter.Button(self.frame, text=option_g, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 5, -5), self.newWindow2('bQuest4', 'Question 4')])
        question.pack(padx=20, pady=15)
        h.pack(pady=5)
        s.pack(pady=5)
        g.pack(pady=5)

    def bQuest4(self):

        question_description = "The controversial Thursday night football game is tonight, and you have an 8 am class " \
                               "in the morning. Do you: "
        option_h = "Be a supportive Ag and go to the game but also be up in time for class."
        option_s = "Be the redass Aggie that you are and just go to the game. You’re really only here for football " \
                   "anyways. "
        option_g = "Who cares about football? You’ll be in class though."
        question = tkinter.Label(self.frame, text=question_description, wraplength=500, bg='white')
        h = tkinter.Button(self.frame, text=option_h, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(-5, 5, 5), self.newWindow2('bQuest5', 'Question 5')])
        s = tkinter.Button(self.frame, text=option_s, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, -5, 5), self.newWindow2('bQuest5', 'Question 5')])
        g = tkinter.Button(self.frame, text=option_g, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 5, -5), self.newWindow2('bQuest5', 'Question 5')])
        question.pack(padx=20, pady=15)
        h.pack(pady=5)
        s.pack(pady=5)
        g.pack(pady=5)

    def bQuest5(self):

        question_description = "Ahh mondays. You’re super tired after this weekend. Maybe you can sleep in and get " \
                               "breakfast instead of class? "
        option_h = "Definitely gonna sleep until noon and eat a “late breakfast"
        option_s = "Meet up with your suitemates for a breakfast date"
        option_g = "No way. What if they take attendance?"
        question = tkinter.Label(self.frame, text=question_description, wraplength=500, bg='white')
        h = tkinter.Button(self.frame, text=option_h, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.newWindow2('bQuest6', 'Question 6'), self.update_health(-5, 5, 5)])
        s = tkinter.Button(self.frame, text=option_s, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, -5, 5), self.newWindow2('bQuest6', 'Question 6')])
        g = tkinter.Button(self.frame, text=option_g, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 5, -5), self.newWindow2('bQuest6', 'Question 6')])
        question.pack(padx=20, pady=15)
        h.pack(pady=5)
        s.pack(pady=5)
        g.pack(pady=5)

    def bQuest6(self):

        question_description = "There is a frat party this weekend and your new found college friends have invited " \
                               "you to come. Should you: "
        option_h = "Go for a run."
        option_s = "Go and have fun! This is your first college party."
        option_g = "Start planning for the week to come."
        question = tkinter.Label(self.frame, text=question_description, wraplength=500, bg='white')
        h = tkinter.Button(self.frame, text=option_h, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(-5, 5, 5), self.newWindow2('bQuest7', 'Question 7')])
        s = tkinter.Button(self.frame, text=option_s, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, -5, 5), self.newWindow2('bQuest7', 'Question 7'), self.popup2()])
        g = tkinter.Button(self.frame, text=option_g, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 5, -5), self.newWindow2('bQuest7', 'Question 7')])
        question.pack(padx=20, pady=15)
        h.pack(pady=5)
        s.pack(pady=5)
        g.pack(pady=5)

    def bQuest7(self):

        question_description = "It’s Tuesday night, aka time for Breakaway! But, you have an exam tomorrow in CSCE " \
                               "222 that you just remembered about. Should you: "
        option_h = "Go to breakaway, but go straight to sleep afterwards. Can’t do well on an exam without sleep!"
        option_s = "Take the time off and go to Breakaway, and stay up until the early hours of the morning studying \n" \
                   "for your exam with your friends. "
        option_g = "Skip breakaway and study at Zachry."
        question = tkinter.Label(self.frame, text=question_description, wraplength=500, bg='white')
        h = tkinter.Button(self.frame, text=option_h, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(-5, 5, 5), self.newWindow2('bQuest8', 'Question 8')])
        s = tkinter.Button(self.frame, text=option_s, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, -5, 5), self.newWindow2('bQuest8', 'Question 8')])
        g = tkinter.Button(self.frame, text=option_g, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 5, -5), self.newWindow2('bQuest8', 'Question 8')])
        question.pack(padx=20, pady=15)
        h.pack(pady=5)
        s.pack(pady=5)
        g.pack(pady=5)

    def bQuest8(self):

        question_description = "Friday night is here, which means it’s time for the weekend! Your roomies have " \
                               "invited you to go out to The Chicken to celebrate! Do you: "
        option_h = "Stay at home and binge the new season of Stranger Things on Netflix. You had a long week!"
        option_s = "Go and spend some quality time with your friends over a plate of cheese fries!"
        option_g = "Offer to order cheese fries to go if your roomies will study with you in ZACH instead :)"
        question = tkinter.Label(self.frame, text=question_description, wraplength=500, bg='white')
        h = tkinter.Button(self.frame, text=option_h, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(-5, 5, 5), self.newWindow2('bQuest9', 'Question 9')])
        s = tkinter.Button(self.frame, text=option_s, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, -5, 5), self.newWindow2('bQuest9', 'Question 9')])
        g = tkinter.Button(self.frame, text=option_g, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 5, -5), self.newWindow2('bQuest9', 'Question 9')])
        question.pack(padx=20, pady=15)
        h.pack(pady=5)
        s.pack(pady=5)
        g.pack(pady=5)

    def bQuest9(self):

        question_description = "It’s the week you’ve been dreading: first exams. How do you prepare?"
        option_h = "Meal prep all your breakfasts and lunches! You won’t have time to think about meals with all that \n" \
                   "studying you’ll be doing."
        option_s = "You talk with your roomies and decide to keep each other accountable! You will make sure everyone \n" \
                   "takes care of themselves and studies hard."
        option_g = "Total study overdrive. Red bull and Evans, here you come!"
        question = tkinter.Label(self.frame, text=question_description, wraplength=500, bg='white')
        h = tkinter.Button(self.frame, text=option_h, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(-5, 5, 5), self.newWindow2('bQuest10', 'Question 10')])
        s = tkinter.Button(self.frame, text=option_s, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, -5, 5), self.newWindow2('bQuest10', 'Question 10')])
        g = tkinter.Button(self.frame, text=option_g, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 5, -5), self.newWindow2('bQuest10', 'Question 10')])
        question.pack(padx=20, pady=15)
        h.pack(pady=5)
        s.pack(pady=5)
        g.pack(pady=5)

    def bQuest10(self):

        question_description = "After that long week, you are really excited to drive home for the first time in " \
                               "forever! Your brother has a football game tonight, and your family has invited you " \
                               "out to support him. However, you put off a programming assignment (that’s due at " \
                               "midnight!!!) to study for all of your exams. Do you: "
        option_h = "Volunteer to help with warm ups! You can exercise and support your family."
        option_s = "Go to the game and cheer the loudest that you can! Family is more important than Homework."
        option_g = "Tell your brother that you will congratulate him with ice cream when he is done, and head \n" \
                   "straight home to finish your assignment."
        question = tkinter.Label(self.frame, text=question_description, wraplength=500, bg='white')
        h = tkinter.Button(self.frame, text=option_h, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(-5, 5, 5), self.newWindow2('bQuest11', 'Question 11')])
        s = tkinter.Button(self.frame, text=option_s, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, -5, 5), self.newWindow2('bQuest11', 'Question 11'), self.popup3()])
        g = tkinter.Button(self.frame, text=option_g, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 5, -5), self.newWindow2('bQuest11', 'Question 11')])
        question.pack(padx=20, pady=15)
        h.pack(pady=5)
        s.pack(pady=5)
        g.pack(pady=5)

    def bQuest11(self):

        question_description = "Whew! First round of midterms are finally over. You have decided that you want to " \
                               "take a little bit of a break this week. Do you: "
        option_h = "Train for that weightlifting competition coming up."
        option_s = "Go out with some friends. Do you even remember what they look like?"
        option_g = "Have some nice time to yourself. You have been meaning to read that book which has been \n" \
                   "collecting dust. "
        question = tkinter.Label(self.frame, text=question_description, wraplength=500, bg='white')
        h = tkinter.Button(self.frame, text=option_h, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(-5, 5, 5), self.newWindow2('bQuest12', 'Question 12'), self.popup4()])
        s = tkinter.Button(self.frame, text=option_s, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, -5, 5), self.newWindow2('bQuest12', 'Question 12'), self.popup5()])
        g = tkinter.Button(self.frame, text=option_g, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 5, -5), self.newWindow2('bQuest12', 'Question 12'), self.popup5()])
        question.pack(padx=20, pady=15)
        h.pack(pady=5)
        s.pack(pady=5)
        g.pack(pady=5)

    def bQuest12(self):

        question_description = "It’s the weekend and your friends have invited you over for a party."
        option_h = "Stay in and do some TLC. This new face mask has been calling your name."
        option_s = "Go to the party. You did say that you were taking a break."
        option_g = "Stay in. You're tired of being around people."
        question = tkinter.Label(self.frame, text=question_description, wraplength=500, bg='white')
        h = tkinter.Button(self.frame, text=option_h, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(-5, 5, 5), self.newWindow2('bQuest13', 'Question 13')])
        s = tkinter.Button(self.frame, text=option_s, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, -5, 5), self.newWindow2('bQuest13', 'Question 13')])
        g = tkinter.Button(self.frame, text=option_g, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 5, -5), self.newWindow2('bQuest13', 'Question 13')])
        question.pack(padx=20, pady=15)
        h.pack(pady=5)
        s.pack(pady=5)
        g.pack(pady=5)

    def bQuest13(self):

        question_description = "Unfortunately the break you decided to take last week has increased " \
                               "your workload this week. Do you: "
        option_h = "Skip class. I really need to get this work done."
        option_s = "Skip class and stay up late. You didn't realize how much work you were procrastinating on."
        option_g = "Go to class. Cheers to late nights at Zachary."
        question = tkinter.Label(self.frame, text=question_description, wraplength=500, bg='white')
        h = tkinter.Button(self.frame, text=option_h, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(-5, 5, 5), self.newWindow2('bQuest14', 'Question 14')])
        s = tkinter.Button(self.frame, text=option_s, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, -5, 5), self.newWindow2('bQuest14', 'Question 14')])
        g = tkinter.Button(self.frame, text=option_g, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 5, -5), self.newWindow2('bQuest14', 'Question 14')])
        question.pack(padx=20, pady=15)
        h.pack(pady=5)
        s.pack(pady=5)
        g.pack(pady=5)

    def bQuest14(self):

        question_description = "After a long week it is finally the weekend. Great time to get ahead on some " \
                               "work or relax a little. Should you: "
        option_h = "Hit up the spa for a massage. School has been very stressful lately."
        option_s = "Have a relaxation weekend. It's been a tough week."
        option_g = "Go to Zachry and get some work done."
        question = tkinter.Label(self.frame, text=question_description, wraplength=500, bg='white')
        h = tkinter.Button(self.frame, text=option_h, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(-5, 5, 5), self.newWindow2('bQuest15', 'Question 15')])
        s = tkinter.Button(self.frame, text=option_s, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, -5, 5), self.newWindow2('bQuest15', 'Question 15')])
        g = tkinter.Button(self.frame, text=option_g, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 5, -5), self.newWindow2('bQuest15', 'Question 15')])
        question.pack(padx=20, pady=15)
        h.pack(pady=5)
        s.pack(pady=5)
        g.pack(pady=5)

    def bQuest15(self):

        question_description = "Lectures have not been useful recently. You take notes in class, ask " \
                               "questions, and pay attention yet you still have to spend hours on the homework. Do " \
                               "you: "
        option_h = "Only skip one class to get your frustration under control. You are paying for this after all."
        option_s = "Skip class and hang out with your friends."
        option_g = "Skip lectures this week. It’s not like they are useful anyway."
        question = tkinter.Label(self.frame, text=question_description, wraplength=500, bg='white')
        h = tkinter.Button(self.frame, text=option_h, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(-5, 5, 5), self.newWindow2('bQuest16', 'Question 16')])
        s = tkinter.Button(self.frame, text=option_s, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, -5, 5), self.newWindow2('bQuest16', 'Question 16')])
        g = tkinter.Button(self.frame, text=option_g, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 5, -5), self.newWindow2('bQuest16', 'Question 16')])
        question.pack(padx=20, pady=15)
        h.pack(pady=5)
        s.pack(pady=5)
        g.pack(pady=5)

    def bQuest16(self):

        question_description = "Your best friend has decided to celebrate their birthday in California this " \
                               "weekend and has invited you. However, a major project is due in your history class " \
                               "this Sunday. Do you: "
        option_h = "Don’t go and instead invest the money that you were going to spend on the trip."
        option_s = "Go!!! You have never been to California and it's your best friend."
        option_g = "Send a birthday gift instead. You really can’t miss the deadline for this project."
        question = tkinter.Label(self.frame, text=question_description, wraplength=500, bg='white')
        h = tkinter.Button(self.frame, text=option_h, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(-5, 5, 5), self.newWindow2('bQuest17', 'Question 17')])
        s = tkinter.Button(self.frame, text=option_s, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, -5, 5), self.newWindow2('bQuest17', 'Question 17'), self.popup6()])
        g = tkinter.Button(self.frame, text=option_g, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 5, -5), self.newWindow2('bQuest17', 'Question 17')])
        question.pack(padx=20, pady=15)
        h.pack(pady=5)
        s.pack(pady=5)
        g.pack(pady=5)

    def bQuest17(self):

        question_description = "There is an event going on this week where tech companies are going to " \
                               "showcase their internships. Do you: "
        option_h = "Don’t go. I’m just going to apply to companies online."
        option_s = "Go and talk to the companies. Maybe they would like your work ethic."
        option_g = "Don’t go because you have not built up enough skill yet. You then spend \n" \
                   "all weekend on learning app development."
        question = tkinter.Label(self.frame, text=question_description, wraplength=500, bg='white')
        h = tkinter.Button(self.frame, text=option_h, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(-5, 5, 5), self.newWindow2('bQuest18', 'Question 18')])
        s = tkinter.Button(self.frame, text=option_s, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, -5, 5), self.newWindow2('bQuest18', 'Question 18'), self.popup7()])
        g = tkinter.Button(self.frame, text=option_g, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 5, -5), self.newWindow2('bQuest18', 'Question 18'), self.popup8()])
        question.pack(padx=20, pady=15)
        h.pack(pady=5)
        s.pack(pady=5)
        g.pack(pady=5)

    def bQuest18(self):

        question_description = "You are really struggling with the latest CSCE 121 programming project. Do you: "
        option_h = "You’ve done decent on the other programming assignments. I will just take a \n" \
                   "hit and not stress over it."
        option_s = "Try your best and figure it out on your own."
        option_g = "Go to office Hours. You really don’t know what you are doing."
        question = tkinter.Label(self.frame, text=question_description, wraplength=500, bg='white')
        h = tkinter.Button(self.frame, text=option_h, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(-5, 5, 5), self.newWindow2('bQuest19', 'Question 19')])
        s = tkinter.Button(self.frame, text=option_s, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, -5, 5), self.newWindow2('bQuest19', 'Question 19')])
        g = tkinter.Button(self.frame, text=option_g, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 5, -5), self.newWindow2('bQuest19', 'Question 19')])
        question.pack(padx=20, pady=15)
        h.pack(pady=5)
        s.pack(pady=5)
        g.pack(pady=5)

    def bQuest19(self):

        question_description = "You got invited to go to a friend’s semi formal this Thursday! But, you know you have a busy week coming up… Do you:"
        option_h = "Say yes and start prepping by going to the gym!"
        option_s = "Ask your friends what they think! They always know best."
        option_g = "Say that you have to stay in and study this weekend."
        question = tkinter.Label(self.frame, text=question_description, wraplength=500, bg='white')
        h = tkinter.Button(self.frame, text=option_h, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(-5, 5, 5), self.newWindow2('bQuest20', 'Question 20')])
        s = tkinter.Button(self.frame, text=option_s, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, -5, 5), self.newWindow2('bQuest20', 'Question 20')])
        g = tkinter.Button(self.frame, text=option_g, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 5, -5), self.newWindow2('bQuest20', 'Question 20')])
        question.pack(padx=20, pady=15)
        h.pack(pady=5)
        s.pack(pady=5)
        g.pack(pady=5)

    def bQuest20(self):

        question_description = "There’s an away game this weekend, and your roomies invited you to go with them! Sure, it’s a 7 hour drive, and you’re exhausted from this week, but they have friends that you can stay with for free! Do you:"
        option_h = "Start packing and hit the road!"
        option_s = "Stay home and rest. You can watch the game on TV while you recover from this week."
        option_g = "Say you’ll go, but only if you can stay at the friend’s house during the game to study."
        question = tkinter.Label(self.frame, text=question_description, wraplength=500, bg='white')
        h = tkinter.Button(self.frame, text=option_h, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(-5, 5, 5), self.newWindow2('bQuest21', 'Question 21')])
        s = tkinter.Button(self.frame, text=option_s, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, -5, 5), self.newWindow2('bQuest21', 'Question 21')])
        g = tkinter.Button(self.frame, text=option_g, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 5, -5), self.newWindow2('bQuest21', 'Question 21')])
        question.pack(padx=20, pady=15)
        h.pack(pady=5)
        s.pack(pady=5)
        g.pack(pady=5)

    def bQuest21(self):

        question_description = "It’s been a particularly busy week, and you have, yet another, major lab " \
                               "report due Friday night. Do you: "
        option_h = "Watch a movie with your roommates and go to bed early to catch up on\n" \
                   "some much needed sleep."
        option_s = "Head over to the rec to play some pickup sand volleyball with some friends \n" \
                   "to relieve some stress."
        option_g = "Burn the midnight oil to get your project done early. You never know what \n" \
                   "problems might come up."
        question = tkinter.Label(self.frame, text=question_description, wraplength=500, bg='white')
        h = tkinter.Button(self.frame, text=option_h, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(-5, 5, 5), self.newWindow2('bQuest22', 'Question 22')])
        s = tkinter.Button(self.frame, text=option_s, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, -5, 5), self.newWindow2('bQuest22', 'Question 22')])
        g = tkinter.Button(self.frame, text=option_g, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 5, -5), self.newWindow2('bQuest22', 'Question 22'), self.popup9()])
        question.pack(padx=20, pady=15)
        h.pack(pady=5)
        s.pack(pady=5)
        g.pack(pady=5)

    def bQuest22(self):

        question_description = "You’ve been invited to your fish camp counselor’s ring dunk. You don’t really " \
                               "know them that well, but you can’t wait to find out what all the hype is about. Do " \
                               "you: "
        option_h = "Go to the dunk, but head out after you’ve congratulated your counselors \n" \
                   "and said hi to a few people. "
        option_s = "Go to the dunk, cheer on your mom and dad, and enjoy a crazy camp reunion!"
        option_g = "Stay home and study. You’ve got the rest of college to go to dunks. "
        question = tkinter.Label(self.frame, text=question_description, wraplength=500, bg='white')
        h = tkinter.Button(self.frame, text=option_h, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(-5, 5, 5), self.newWindow2('bQuest23', 'Question 23')])
        s = tkinter.Button(self.frame, text=option_s, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, -5, 5), self.newWindow2('bQuest23', 'Question 23')])
        g = tkinter.Button(self.frame, text=option_g, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 5, -5), self.newWindow2('bQuest23', 'Question 23')])
        question.pack(padx=20, pady=15)
        h.pack(pady=5)
        s.pack(pady=5)
        g.pack(pady=5)

    def bQuest23(self):

        question_description = "Your computer science club has a sponsored meet and greet this Thursday " \
                               "night with several well known companies that you would love to intern for. "
        option_h = "Forgo the greasy, fast food pizza and eat before you come."
        option_s = "Go for the free pizza, see your friends, and then leave."
        option_g = "Socialize with all of the industry reps, in order to build your knowledge \n" \
                   "base of company interests and what potential internships and research\n" \
                   "possibilities there are. "
        question = tkinter.Label(self.frame, text=question_description, wraplength=500, bg='white')
        h = tkinter.Button(self.frame, text=option_h, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(-5, 5, 5), self.newWindow2('bQuest24', 'Question 24')])
        s = tkinter.Button(self.frame, text=option_s, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, -5, 5), self.newWindow2('bQuest24', 'Question 24')])
        g = tkinter.Button(self.frame, text=option_g, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 5, -5), self.newWindow2('bQuest24', 'Question 24')])
        question.pack(padx=20, pady=15)
        h.pack(pady=5)
        s.pack(pady=5)
        g.pack(pady=5)

    def bQuest24(self):

        question_description = "It’s the biggest football game of the season, your friend from high school" \
                               "came in just for the game on Saturday, and you have that big test on Monday. Do you:"
        option_h = "You take a nap on Friday before your friend gets there because you know \n" \
                   "that you are going to take her to Midnight Yell. Then you will have the \n" \
                   "energy to show her around campus before the game."
        option_s = "Put everything off so that you can show your friend the full Aggie \n" \
                   "experience. She’s leaving after the game anyways, so you’ll have the rest \n" \
                   "of the weekend to study."
        option_g = "After you show her around campus some, you go to The Brew so that you\n" \
                   "both can get some last minute studying in before the game."
        question = tkinter.Label(self.frame, text=question_description, wraplength=500, bg='white')
        h = tkinter.Button(self.frame, text=option_h, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(-5, 5, 5), self.newWindow2('bQuest25', 'Question 25')])
        s = tkinter.Button(self.frame, text=option_s, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, -5, 5), self.newWindow2('bQuest25', 'Question 25'), self.popup10()])
        g = tkinter.Button(self.frame, text=option_g, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 5, -5), self.newWindow2('bQuest25', 'Question 25')])
        question.pack(padx=20, pady=15)
        h.pack(pady=5)
        s.pack(pady=5)
        g.pack(pady=5)

    def bQuest25(self):

        question_description = "Thanksgiving is next week, you have several projects due the following week," \
                               "but you will be in the middle of nowhere with your family with no internet service. " \
                               "Do you: "
        option_h = "Go grocery shopping and meal prep now, so that you can focus on your\n" \
                   "project and still eat healthy when you get back."
        option_s = "Get started now, but find the nearest Starbucks to work at while you're \n" \
                   "gone. There’s no way you would leave early and miss out on all of the fun. \n" \
                   "#FOMO is a real thing."
        option_g = "Start working on them now, but plan to come back early and get some \n" \
                   "undivided time to work on your projects. "
        question = tkinter.Label(self.frame, text=question_description, wraplength=500, bg='white')
        h = tkinter.Button(self.frame, text=option_h, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(-5, 5, 5), self.newWindow2('bQuest26', 'Question 26')])
        s = tkinter.Button(self.frame, text=option_s, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, -5, 5), self.newWindow2('bQuest26', 'Question 26')])
        g = tkinter.Button(self.frame, text=option_g, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 5, -5), self.newWindow2('bQuest26', 'Question 26')])
        question.pack(padx=20, pady=15)
        h.pack(pady=5)
        s.pack(pady=5)
        g.pack(pady=5)

    def bQuest26(self):

        question_description = "With Thanksgiving break approaching, and plans from family and friends" \
                               "continue to multiply, you are tempted with the idea of skipping your last classes" \
                               "to start your break early. Everyone else is doing it, and no new material will be " \
                               "covered anyways... Do you:"
        option_h = "You decide to head home early to get some well-deserved TLC from your \n" \
                   "Mom before y’all go out of town. You can’t take anymore of the same \n" \
                   "boring options from Sbisa."
        option_s = "Get a peer to take notes for you, while you go play frisbee with your\n" \
                   "friends before not seeing each other for a whole week."
        option_g = "You decided to suck it up and stay to take notes for all of your friends.\n"
        question = tkinter.Label(self.frame, text=question_description, wraplength=500, bg='white')
        h = tkinter.Button(self.frame, text=option_h, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(-5, 5, 5), self.newWindow2('bQuest27', 'Question 27')])
        s = tkinter.Button(self.frame, text=option_s, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, -5, 5), self.newWindow2('bQuest27', 'Question 27')])
        g = tkinter.Button(self.frame, text=option_g, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 5, -5), self.newWindow2('bQuest27', 'Question 27'), self.popup11()])
        question.pack(padx=20, pady=15)
        h.pack(pady=5)
        s.pack(pady=5)
        g.pack(pady=5)

    def bQuest27(self):

        question_description = "Your registration time begins at 5:45am tomorrow morning. Do you: "
        option_h = "You don’t want to miss your registration time, so you go to bed extra early."
        option_s = "Stay up all night at iHop with a friend in order to not oversleep and be\n" \
                   "prepared with schedule options by 5:45am."
        option_g = "Your schedule options have already been planned for weeks, so you work \n" \
                   "on homework, go to bed at your normal time, and wake up 30 minutes \n" \
                   "early to register. "
        question = tkinter.Label(self.frame, text=question_description, wraplength=500, bg='white')
        h = tkinter.Button(self.frame, text=option_h, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(-5, 5, 5), self.newWindow2('bQuest28', 'Question 28')])
        s = tkinter.Button(self.frame, text=option_s, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, -5, 5), self.newWindow2('bQuest28', 'Question 28'), self.popup12()])
        g = tkinter.Button(self.frame, text=option_g, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 5, -5), self.newWindow2('bQuest28', 'Question 28')])
        question.pack(padx=20, pady=15)
        h.pack(pady=5)
        s.pack(pady=5)
        g.pack(pady=5)

    def bQuest28(self):

        question_description = "All of your friends are basically done for the semester (you know, some of " \
                               "those RPTS majors..) and ask you over for a game night. Do you:"
        option_h = "Tell your friends that you won’t be there until later and go through with\n" \
                   "your plans to attend that Pilates class at the rec, followed by a nutritious \n" \
                   "home-cooked meal."
        option_s = "Tell your friends that you’ll bring the dominos if they bring the snacks. It’s\n" \
                   "past time for some 42!"
        option_g = "Are you kidding?! I still have 3 finals, 4 projects, a presentation, and 2 lab \n" \
                   "reports due. There is no time for games. Even if it is 42."
        question = tkinter.Label(self.frame, text=question_description, wraplength=500, bg='white')
        h = tkinter.Button(self.frame, text=option_h, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(-5, 5, 5), self.newWindow2('bQuest29', 'Question 29')])
        s = tkinter.Button(self.frame, text=option_s, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, -5, 5), self.newWindow2('bQuest29', 'Question 29')])
        g = tkinter.Button(self.frame, text=option_g, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 5, -5), self.newWindow2('bQuest29', 'Question 29')])
        question.pack(padx=20, pady=15)
        h.pack(pady=5)
        s.pack(pady=5)
        g.pack(pady=5)

    def bQuest29(self):

        question_description = "Finals season is upon us, and it’s reading day. How do you decide to spend" \
                               "your class-free day?"
        option_h = "You’ve been working hard lately, it’s time to rest and binge some Netflix."
        option_s = "No class means no schoolwork! Take the day off and hang out with friends."
        option_g = "The semester is almost over, push through and study some more."
        question = tkinter.Label(self.frame, text=question_description, wraplength=500, bg='white')
        h = tkinter.Button(self.frame, text=option_h, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(-5, 5, 5), self.newWindow2('bQuest30', 'Question 30')])
        s = tkinter.Button(self.frame, text=option_s, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, -5, 5), self.newWindow2('bQuest30', 'Question 30')])
        g = tkinter.Button(self.frame, text=option_g, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 5, -5), self.newWindow2('bQuest30', 'Question 30')])
        question.pack(padx=20, pady=15)
        h.pack(pady=5)
        s.pack(pady=5)
        g.pack(pady=5)

    def bQuest30(self):

        question_description = "You’ve taken your first final, and your next one isn’t for a whole week! You" \
                               "have no classes, no projects, and no papers to worry about, and your friends " \
                               "want to take a quick road trip before going home for break."
        option_h = "Your body isn’t in any state to go on a trip! You’ve been pulling all-nighters, \n" \
                   "finishing projects, and living off of your remaining meal trades. You decide\n" \
                   "to spend the first two days sleeping, study for two days, clean your dorm,\n" \
                   "pack to go home, go on a run, and review exam material while feeling \n" \
                   "rested to conquer your day on campus! "
        option_s = "What are we waiting for? Let’s load up and roll out!! So.. Where are we going? "
        option_g = "You’re so close, push through, you have all break to sleep and hang out. \n" \
                   "Friday: study chapters 1-4, Saturday: chapters 5-8, Sunday: \n" \
                   "chapters 9-12, Monday: chapters 13-15, Tuesday: review semester notes, \n" \
                   "Wednesday: study old tests, Thursday: ace exam!! "
        question = tkinter.Label(self.frame, text=question_description, wraplength=500, bg='white')
        h = tkinter.Button(self.frame, text=option_h, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(-5, 5, 5), self.newWindow2('game_over', 'Game Over!')])
        s = tkinter.Button(self.frame, text=option_s, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, -5, 5), self.newWindow2('game_over', 'Game Over!')])
        g = tkinter.Button(self.frame, text=option_g, bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 5, -5), self.newWindow2('game_over', 'Game Over!')])
        question.pack(padx=20, pady=15)
        h.pack(pady=5)
        s.pack(pady=5)
        g.pack(pady=5)


    def game_over(self):
        health = self.h_bar
        social = self.s_bar
        gpa = self.g_bar
        stats = tkinter.Label(self.frame, text="Health: " + repr(health) + "\nSocial: " + repr(social) + "\nGPA: " + repr(gpa), bg='white')
        start_over = tkinter.Button(self.frame, text="Play Again", bg='white', command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.reset(), self.update_health(100, 100, 100), self.newWindow2('bQuest1', 'Question 1')])
        stats.pack()
        start_over.pack()