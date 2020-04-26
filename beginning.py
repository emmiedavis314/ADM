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
        option_h = "Meal prep for the coming week."
        option_s = "Party it UPPPP!!! It’s college; you are supposed to make mistakes."
        option_g = "Stay home and study."
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
        option_h = "Go to the gym and get swole. I can start on it tomorrow."
        option_s = "Procrastinate and play Animal Crossing with some friends, it’s not due until next week anyway.(If " \
                   "they choose this option then have a pop up stating that they had to turn the project in late) "
        option_g = "Start early, you have never coded before."
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
        option_h = "Be a supportive Ag and go to the game but also be up in time for class."
        option_s = "Be the redass Aggie that you are and just go to the game. You’re really only here for football " \
                   "anyways. "
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
        option_h = "Go for a run."
        option_s = "Go and have fun! This is your first college party. (random event: cops got called, and everyone " \
                   "underaged went to jail.)"
        option_g = "Start planning for the week to come."
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
        option_h = "Go to breakaway, but go straight to sleep afterwards. Can’t do well on an exam without sleep!"
        option_s = "Take the time off and go to Breakaway, and stay up until the early hours of the morning studying " \
                   "for your exam with your friends. "
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
        option_h = "Stay at home and binge the new season of Stranger Things on Netflix. You had a long week!"
        option_s = "Go and spend some quality time with your friends over a plate of cheese fries!"
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
                   "studying you’ll be doing."
        option_s = "You talk with your roomies and decide to keep each other accountable! You will make sure everyone " \
                   "takes care of themselves and studies hard."
        option_g = "Total study overdrive. Red bull and Evans, here you come!"
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
        option_h = "Volunteer to help with warm ups! You can exercise and support your family."
        option_s = "Go to the game and cheer the loudest that you can! Family is more important than Homework.(popup " \
                   "with a more decrease to GPA)"
        option_g = "Tell your brother that you will congratulate him with ice cream when he is done, and head " \
                   "straight home to finish your assignment."
        question = Label(self.frame, text=question_description)
        h = Button(self.frame, text=option_h, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(0, 5, 5), self.newWindow2('bQuest11', 'question 11')])
        s = Button(self.frame, text=option_s, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 0, 5), self.newWindow2('bQuest11', 'question 11')])
        g = Button(self.frame, text=option_g, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 5, 0), self.newWindow2('bQuest11', 'question 11')])
        question.pack()
        h.pack()
        s.pack()
        g.pack()

    def bQuest11(self):

        question_description = "Whew! First round of midterms are finally over. You have decided that you want to " \
                               "take a little bit of a break this week. Do you: "
        option_h = "Train for that weightlifting competition coming up.(popup. Win the weightlifting competition)"
        option_s = "Go out with some friends. Do you even remember what they look like?"
        option_g = "Have some nice time to yourself. You have been meaning to read that book which has been collecting dust."
        question = Label(self.frame, text=question_description)
        h = Button(self.frame, text=option_h, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(0, 5, 5), self.newWindow2('bQuest12', 'question 12')])
        s = Button(self.frame, text=option_s, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 0, 5), self.newWindow2('bQuest12', 'question 12')])
        g = Button(self.frame, text=option_g, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 5, 0), self.newWindow2('bQuest12', 'question 12')])
        question.pack()
        h.pack()
        s.pack()
        g.pack()

    def bQuest12(self):

        question_description = "It’s the weekend and your friends have invited you over for a party."
        option_h = "Stay in and do some TLC. This new face mask has been calling your name."
        option_s = "Go to the party. You did say that you were taking a break."
        option_g = "Stay in. You're tired of being around people."
        question = Label(self.frame, text=question_description)
        h = Button(self.frame, text=option_h, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(0, 5, 5), self.newWindow2('bQuest13', 'question 13')])
        s = Button(self.frame, text=option_s, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 0, 5), self.newWindow2('bQuest13', 'question 13')])
        g = Button(self.frame, text=option_g, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 5, 0), self.newWindow2('bQuest13', 'question 13')])
        question.pack()
        h.pack()
        s.pack()
        g.pack()

    def bQuest13(self):

        question_description = "Unfortunately the break you decided to take last week has increased " \
                               "your workload this week. Do you: "
        option_h = "Skip class. I really need to get this work done."
        option_s = "Skip class and stay up late. You didn’t realize how much work you were procrastinating on."
        option_g = "Go to class. Cheers to late nights at Zachary."
        question = Label(self.frame, text=question_description)
        h = Button(self.frame, text=option_h, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(0, 5, 5), self.newWindow2('bQuest14', 'question 14')])
        s = Button(self.frame, text=option_s, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 0, 5), self.newWindow2('bQuest14', 'question 14')])
        g = Button(self.frame, text=option_g, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 5, 0), self.newWindow2('bQuest14', 'question 14')])
        question.pack()
        h.pack()
        s.pack()
        g.pack()

    def bQuest14(self):

        question_description = "After a long week it is finally the weekend. Great time to get ahead on some " \
                               "work or relax a little. Should you: "
        option_h = "Hit up the spa for a massage. School has been very stressful lately."
        option_s = "Have a relaxation weekend. It's been a tough week."
        option_g = "Go to Zachry and get some work done."
        question = Label(self.frame, text=question_description)
        h = Button(self.frame, text=option_h, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(0, 5, 5), self.newWindow2('bQuest15', 'question 15')])
        s = Button(self.frame, text=option_s, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 0, 5), self.newWindow2('bQuest15', 'question 15')])
        g = Button(self.frame, text=option_g, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 5, 0), self.newWindow2('bQuest15', 'question 15')])
        question.pack()
        h.pack()
        s.pack()
        g.pack()

    def bQuest15(self):

        question_description = "Lectures have not been useful recently. You take notes in class, ask " \
                               "questions, and pay attention yet you still have to spend hours on the homework. Do you: "
        option_h = "Only skip one class to get your frustration under control. You are paying for this after all."
        option_s = "Skip class and hang out with your friends."
        option_g = "Skip lectures this week. It’s not like they are useful anyway."
        question = Label(self.frame, text=question_description)
        h = Button(self.frame, text=option_h, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(0, 5, 5), self.newWindow2('bQuest16', 'question 16')])
        s = Button(self.frame, text=option_s, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 0, 5), self.newWindow2('bQuest16', 'question 16')])
        g = Button(self.frame, text=option_g, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 5, 0), self.newWindow2('bQuest16', 'question 16')])
        question.pack()
        h.pack()
        s.pack()
        g.pack()

    def bQuest16(self):

        question_description = "Your best friend has decided to celebrate their birthday in California this " \
                               "weekend and has invited you. However, a major project is due in your history class " \
                               "this Sunday. Do you: "
        option_h = "Don’t go and instead invest the money that you were going to spend on the trip."
        option_s = "Go!!! You have never been to California and it's your best friend. (random: The flight on the way " \
                   "back was delayed and the WiFi on the plane was not working. You couldn’t finish the project in time " \
                   "and you had to beg the professor to let you turn it in late.)"
        option_g = "Send a birthday gift instead. You really can’t miss the deadline for this project."
        question = Label(self.frame, text=question_description)
        h = Button(self.frame, text=option_h, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(0, 5, 5), self.newWindow2('bQuest17', 'question 17')])
        s = Button(self.frame, text=option_s, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 0, 5), self.newWindow2('bQuest17', 'question 17')])
        g = Button(self.frame, text=option_g, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 5, 0), self.newWindow2('bQuest17', 'question 17')])
        question.pack()
        h.pack()
        s.pack()
        g.pack()

    def bQuest17(self):

        question_description = "There is an event going on this week where tech companies are going to " \
                               "showcase their internships. Do you: "
        option_h = "Don’t go. I’m just going to apply to companies online."
        option_s = "Go and talk to the companies. Maybe they would like your work ethic. " \
                   "(random: The event was during one of your classes and you missed an attendance " \
                   "grade. It would’ve been worth it, but the companies just told you to apply online " \
                   "and it’s unlikely you will get a callback because they don’t hire freshmen."
        option_g = "Don’t go because you have not built up enough skill yet. You then spend " \
                   "all weekend on learning app development."
        question = Label(self.frame, text=question_description)
        h = Button(self.frame, text=option_h, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(0, 5, 5), self.newWindow2('bQuest18', 'question 18')])
        s = Button(self.frame, text=option_s, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 0, 5), self.newWindow2('bQuest18', 'question 18')])
        g = Button(self.frame, text=option_g, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 5, 0), self.newWindow2('bQuest18', 'question 18')])
        question.pack()
        h.pack()
        s.pack()
        g.pack()

    def bQuest18(self):

        question_description = "You are really struggling with the latest CSCE 121 programming project. Do you: "
        option_h = "You’ve done decent on the other programming assignments. I will just take a " \
                   "hit and not stress over it."
        option_s = "Try your best and figure it out on your own."
        option_g = "Go to office Hours. You really don’t know what you are doing."
        question = Label(self.frame, text=question_description)
        h = Button(self.frame, text=option_h, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(0, 5, 5), self.newWindow2('bQuest19', 'question 19')])
        s = Button(self.frame, text=option_s, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 0, 5), self.newWindow2('bQuest19', 'question 19')])
        g = Button(self.frame, text=option_g, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 5, 0), self.newWindow2('bQuest19', 'question 19')])
        question.pack()
        h.pack()
        s.pack()
        g.pack()

    def bQuest19(self):

        question_description = ""
        option_h = ""
        option_s = ""
        option_g = ""
        question = Label(self.frame, text=question_description)
        h = Button(self.frame, text=option_h, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(0, 5, 5), self.newWindow2('bQuest20', 'question 20')])
        s = Button(self.frame, text=option_s, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 0, 5), self.newWindow2('bQuest20', 'question 20')])
        g = Button(self.frame, text=option_g, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 5, 0), self.newWindow2('bQuest20', 'question 20')])
        question.pack()
        h.pack()
        s.pack()
        g.pack()

    def bQuest20(self):

        question_description = ""
        option_h = ""
        option_s = ""
        option_g = ""
        question = Label(self.frame, text=question_description)
        h = Button(self.frame, text=option_h, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(0, 5, 5), self.newWindow2('bQuest21', 'question 21')])
        s = Button(self.frame, text=option_s, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 0, 5), self.newWindow2('bQuest21', 'question 21')])
        g = Button(self.frame, text=option_g, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 5, 0), self.newWindow2('bQuest21', 'question 21')])
        question.pack()
        h.pack()
        s.pack()
        g.pack()

    def bQuest21(self):

        question_description = "It’s been a particularly busy week, and you have, yet another, major lab " \
                               "report due Friday night. Do you: "
        option_h = "Watch a movie with your roommates and go to bed early to catch up on" \
                   "some much needed sleep."
        option_s = "Head over to the rec to play some pickup sand volleyball with some friends " \
                   "to relieve some stress."
        option_g = "Burn the midnight oil to get your project done early. You never know what " \
                   "problems might come up. (random: you get sick because you haven’t " \
                   "been eating well or getting enough sleep, and therefore have to turn your " \
                   "paper in late) "
        question = Label(self.frame, text=question_description)
        h = Button(self.frame, text=option_h, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(0, 5, 5), self.newWindow2('bQuest22', 'question 22')])
        s = Button(self.frame, text=option_s, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 0, 5), self.newWindow2('bQuest22', 'question 22')])
        g = Button(self.frame, text=option_g, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 5, 0), self.newWindow2('bQuest22', 'question 22')])
        question.pack()
        h.pack()
        s.pack()
        g.pack()

    def bQuest22(self):

        question_description = "You’ve been invited to your fish camp counselor’s ring dunk. You don’t really " \
                               "know them that well, but you can’t wait to find out what all the hype is about. Do you: "
        option_h = "Go to the dunk, but head out after you’ve congratulated your counselors " \
                   "and said hi to a few people. "
        option_s = "Go to the dunk, cheer on your mom and dad, and enjoy a crazy camp reunion!"
        option_g = "Stay home and study. You’ve got the rest of college to go to dunks. "
        question = Label(self.frame, text=question_description)
        h = Button(self.frame, text=option_h, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(0, 5, 5), self.newWindow2('bQuest23', 'question 23')])
        s = Button(self.frame, text=option_s, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 0, 5), self.newWindow2('bQuest23', 'question 23')])
        g = Button(self.frame, text=option_g, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 5, 0), self.newWindow2('bQuest23', 'question 23')])
        question.pack()
        h.pack()
        s.pack()
        g.pack()

    def bQuest23(self):

        question_description = "Your computer science club has a sponsored meet and greet this Thursday " \
                               "night with several well known companies that you would love to intern for. "
        option_h = "Forgo the greasy, fast food pizza and eat before you come."
        option_s = "Go for the free pizza, see your friends, and then leave."
        option_g = "Socialize with all of the industry reps, in order to build your knowledge " \
                   "base of company interests and what potential internships and research" \
                   "possibilities there are. "
        question = Label(self.frame, text=question_description)
        h = Button(self.frame, text=option_h, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(0, 5, 5), self.newWindow2('bQuest24', 'question 24')])
        s = Button(self.frame, text=option_s, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 0, 5), self.newWindow2('bQuest24', 'question 24')])
        g = Button(self.frame, text=option_g, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 5, 0), self.newWindow2('bQuest24', 'question 24')])
        question.pack()
        h.pack()
        s.pack()
        g.pack()

    def bQuest24(self):

        question_description = "It’s the biggest football game of the season, your friend from high school" \
                               "came in just for the game on Saturday, and you have that big test on Monday. Do you:"
        option_h = "You take a nap on Friday before your friend gets there because you know " \
                   "that you are going to take her to Midnight Yell. Then you will have the " \
                   "energy to show her around campus before the game."
        option_s = "Put everything off so that you can show your friend the full Aggie " \
                   "experience. She’s leaving after the game anyways, so you’ll have the rest " \
                   "of the weekend to study. (Random: her battery dies and has to stay a few " \
                   "extra days, so you have to cram for the test on Monday morning.)"
        option_g = "After you show her around campus some, you go to The Brew so that you" \
                   "both can get some last minute studying in before the game."
        question = Label(self.frame, text=question_description)
        h = Button(self.frame, text=option_h, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(0, 5, 5), self.newWindow2('bQuest25', 'question 25')])
        s = Button(self.frame, text=option_s, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 0, 5), self.newWindow2('bQuest25', 'question 25')])
        g = Button(self.frame, text=option_g, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 5, 0), self.newWindow2('bQuest25', 'question 25')])
        question.pack()
        h.pack()
        s.pack()
        g.pack()

    def bQuest25(self):

        question_description = "Thanksgiving is next week, you have several projects due the following week," \
                               "but you will be in the middle of nowhere with your family with no internet service. Do you:"
        option_h = "Go grocery shopping and meal prep now, so that you can focus on your" \
                   "project and still eat healthy when you get back."
        option_s = "Get started now, but find the nearest Starbucks to work at while you're " \
                   "gone. There’s no way you would leave early and miss out on all of the fun. " \
                   "#FOMO is a real thing."
        option_g = "Start working on them now, but plan to come back early and get some " \
                   "undivided time to work on your projects. "
        question = Label(self.frame, text=question_description)
        h = Button(self.frame, text=option_h, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(0, 5, 5), self.newWindow2('bQuest26', 'question 26')])
        s = Button(self.frame, text=option_s, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 0, 5), self.newWindow2('bQuest26', 'question 26')])
        g = Button(self.frame, text=option_g, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 5, 0), self.newWindow2('bQuest26', 'question 26')])
        question.pack()
        h.pack()
        s.pack()
        g.pack()

    def bQuest26(self):

        question_description = "With Thanksgiving break approaching, and plans from family and friends" \
                               "continue to multiply, you are tempted with the idea of skipping your last classes" \
                               "to start your break early. Everyone else is doing it, and no new material will be " \
                               "covered anyways... Do you:"
        option_h = "You decide to head home early to get some well-deserved TLC from your " \
                   "Mom before y’all go out of town. You can’t take anymore of the same " \
                   "boring options from Sbisa."
        option_s = "Get a peer to take notes for you, while you go play frisbee with your" \
                   "friends before not seeing each other for a whole week."
        option_g = "You decided to suck it up and stay to take notes for all of your friends." \
                   "(random: Pop quiz! Good thing you were present. Professor KillJoy’s " \
                   "random question about the color of his shirt earned you 10 bonus points " \
                   "on the next test.)"
        question = Label(self.frame, text=question_description)
        h = Button(self.frame, text=option_h, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(0, 5, 5), self.newWindow2('bQuest27', 'question 27')])
        s = Button(self.frame, text=option_s, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 0, 5), self.newWindow2('bQuest27', 'question 27')])
        g = Button(self.frame, text=option_g, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 5, 0), self.newWindow2('bQuest27', 'question 27')])
        question.pack()
        h.pack()
        s.pack()
        g.pack()

    def bQuest27(self):

        question_description = "Your registration time begins at 5:45am tomorrow morning. Do you: "
        option_h = "You don’t want to miss your registration time, so you go to bed extra early."
        option_s = "Stay up all night at iHop with a friend in order to not oversleep and be" \
                   "prepared with schedule options by 5:45am. (random: In all your efforts to " \
                   "not oversleep by staying up all night, you fall asleep 5 minutes before your" \
                   "registration time, and some of your classes fill up.)"
        option_g = "Your schedule options have already been planned for weeks, so you work " \
                   "on homework, go to bed at your normal time, and wake up 30 minutes " \
                   "early to register. "
        question = Label(self.frame, text=question_description)
        h = Button(self.frame, text=option_h, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(0, 5, 5), self.newWindow2('bQuest28', 'question 28')])
        s = Button(self.frame, text=option_s, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 0, 5), self.newWindow2('bQuest28', 'question 28')])
        g = Button(self.frame, text=option_g, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 5, 0), self.newWindow2('bQuest28', 'question 28')])
        question.pack()
        h.pack()
        s.pack()
        g.pack()

    def bQuest28(self):

        question_description = "All of your friends are basically done for the semester (you know, some of " \
                               "those RPTS majors..) and ask you over for a game night. Do you:"
        option_h = "Tell your friends that you won’t be there until later and go through with" \
                   "your plans to attend that Pilates class at the rec, followed by a nutritious " \
                   "home-cooked meal."
        option_s = "Tell your friends that you’ll bring the dominos if they bring the snacks. It’s" \
                   "past time for some 42!"
        option_g = "Are you kidding?! I still have 3 finals, 4 projects, a presentation, and 2 lab " \
                   "reports due. There is no time for games. Even if it is 42."
        question = Label(self.frame, text=question_description)
        h = Button(self.frame, text=option_h, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(0, 5, 5), self.newWindow2('bQuest29', 'question 29')])
        s = Button(self.frame, text=option_s, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 0, 5), self.newWindow2('bQuest29', 'question 29')])
        g = Button(self.frame, text=option_g, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 5, 0), self.newWindow2('bQuest29', 'question 29')])
        question.pack()
        h.pack()
        s.pack()
        g.pack()

    def bQuest29(self):

        question_description = "Finals season is upon us, and it’s reading day. How do you decide to spend" \
                               "your class-free day?"
        option_h = "You’ve been working hard lately, it’s time to rest and binge some Netflix."
        option_s = "No class means no schoolwork! Take the day off and hang out with friends."
        option_g = "The semester is almost over, push through and study some more."
        question = Label(self.frame, text=question_description)
        h = Button(self.frame, text=option_h, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(0, 5, 5), self.newWindow2('bQuest30', 'question 30')])
        s = Button(self.frame, text=option_s, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 0, 5), self.newWindow2('bQuest30', 'question 30')])
        g = Button(self.frame, text=option_g, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 5, 0), self.newWindow2('bQuest30', 'question 30')])
        question.pack()
        h.pack()
        s.pack()
        g.pack()

    def bQuest30(self):

        question_description = "You’ve taken your first final, and your next one isn’t for a whole week! You" \
                               "have no classes, no projects, and no papers to worry about, and your friends " \
                               "want to take a quick road trip before going home for break."
        option_h = "Your body isn’t in any state to go on a trip! You’ve been pulling all-nighters, " \
                   "finishing projects, and living off of your remaining meal trades. You decide" \
                   "to spend the first two days sleeping, study for two days, clean your dorm," \
                   "pack to go home, go on a run, and review exam material while feeling " \
                   "rested to conquer your day on campus! "
        option_s = "What are we waiting for? Let’s load up and roll out!! So.. Where are we going? "
        option_g = "You’re so close, push through, you have all break to sleep and hang out. " \
                   "Friday: study chapters 1-4, Saturday: chapters 5-8, Sunday: " \
                   "chapters 9-12, Monday: chapters 13-15, Tuesday: review semester notes, " \
                   "Wednesday: study old tests, Thursday: ace exam!! "
        question = Label(self.frame, text=question_description)
        h = Button(self.frame, text=option_h, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(0, 5, 5), self.newWindow2('bQuest1', 'question 1')])
        s = Button(self.frame, text=option_s, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 0, 5), self.newWindow2('bQuest1', 'question 1')])
        g = Button(self.frame, text=option_g, command=lambda: [Begin.bQuest2(self), self.frame.pack_forget(), self.update_health(5, 5, 0), self.newWindow2('bQuest1', 'question 1')])
        question.pack()
        h.pack()
        s.pack()
        g.pack()