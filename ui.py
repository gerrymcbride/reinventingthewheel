import tkinter as tk

LARGE_FONT = ("Verdana", 12)

class newclass(tk.Tk):

	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		main_page = tk.Frame(self)
		main_page.pack(side="top", fill="both", expand = True)

		main_page.grid_rowconfigure(0, weight=1)
		main_page.grid_columnconfigure(0, weight=1)

		self.frames = {}
		for F in (StartPage, PageOne):

		    frame = StartPage(main_page, self)
		    self.frames[F] = frame
		    frame.grid(row=0, column=0, sticky="nsew")


		self.show_frame(StartPage)

	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()


def fag():
	print("poo")

class StartPage(tk.Frame):
	def __init__(self, parent, controller):
	    tk.Frame.__init__(self, parent)
	    label = tk.Label(self, text="StartPage", font=LARGE_FONT)
	    label.pack(pady=10, padx=10)

	    button1 = tk.Button(self, text="Visit Page 1", 
	    	command=lambda: controller.show_frame(PageOne))
	    button1.pack()

class PageOne (tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="New", font=LARGE_FONT)
		label.pack(pady=10,padx=10)

		button2 = tk.Button(self, text="New buttooooooooo", 
			command=lambda: controller.show_frame(StartPage))
		button2.pack()







app = newclass()
app.mainloop()