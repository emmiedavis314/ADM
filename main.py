'''
Title: Aggie Decision Maker

Description: Text based game decision maker game for our CSCE 445 class where users will mimic college life of a sudent
majoring in Computer Science and make decisons that have
have an effect on GPA, health, and grades. Also be an option to play in the compare the different experiences.

Authors: Natalie Burks, Emily Davis, and Alli Reuthinger
'''

#imports
from tkinter import *
from Gui import *
from beginning import Begin
from middle import Middle
from end import End
'''
def menuStarter():
    gui = GUI()
    gui.menu()
    gui.footer()
    gui.MainWindow.mainloop()

def gameStarter():
    gui = GUI()
    gui.healthbars(100,70,50)
    gui.MainWindow.mainloop()

menuStarter()
'''

'''
class Buttons:
	
	def __init__(self, master):
		self.master = master
		self.frame = Frame(self.master)
		self.b1 = Button(self.master, text="Button1", command=self.display)
		self.b2 = Button(self.master, text="Button2", command=self.new_window)
		self.b1.pack()
		self.b2.pack()
		self.frame.pack()

	def display(self):
		print ('Hello Button1')

	def new_window(self):
		self.master.withdraw()
		self.newWindow = Toplevel(self.master)
		bb = Buttons1(self.newWindow)



class Buttons1():
	
	def __init__(self, master):
		self.master = master
		self.frame = Frame(self.master)
		self.b3 = Button(self.master, text="Button3", command=self.display3)
		self.b3.pack()
		self.frame.pack()
		

	def display3(self):
		print ('hello button3')
'''

if __name__ == '__main__':

	root = Tk()
	#root.geometry('250x250')
	root['bg'] = '#500000'
	b = menu(root)
	root.mainloop()

#creating the GUI object

#creating the beginning class

#creating the middle class

#creating the ending class
