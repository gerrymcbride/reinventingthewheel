from tkinter import *
import tkinter as tk



class Start_Window (Frame):
	#count = 0

	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.master = master
		self.init_window()
# main window logic
	def init_window(self):
		self.master.title("GUI")
		self.pack(fill=BOTH, expand=1)
		quitButton = Button(self, text="Quit", command=self.client_exit)
		quitButton.place(x=199, y=450)

		testButton = Button(self, text = "Test", command=self.new_window)
		testButton.place(x=50, y = 50)
# menu & buttons
		menu = Menu(self.master)
		self.master.config(menu=menu)
		file = Menu(menu)
		file.add_command(label='Help', command=self.client_exit)
		file.add_command(label='Exit', command=self.client_exit)
		menu.add_cascade(label='File', menu=file)

# when sum option is chosen
	def new_window(self):
		#self.count += 1
#		window = tk.Toplevel(self)
		self.e = StringVar()
		self.n = Entry(self.master, textvariable=self.e)
		self.n.pack(padx=40, pady=200)

		self.submit = Button(self, text="Submit", command=self.client_exit)
		self.submit.pack(padx=100, pady=200)

#		submitButton = Button(self, text="Submit", command=print("boobs"))
#		submitButton.pack(padx=60, pady=250)
#		label= tk.Label(window, text=self.e)
#		label.pack(side="top", fill="both", padx=4, pady=4)

#######################################################

#exit method
	def client_exit(self):
		exit()

class Second_Window(Frame):
		def __init__(self, master=None):
		    Frame.__init__(self, master)
		    self.master = master
		    self.init_window()






root = Tk()

app = Start_Window(root)

root.geometry("400x500")

root.mainloop()