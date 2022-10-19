import tkinter as tk
from tkinter import ttk


LARGEFONT =("Verdana", 35)

class tkinterApp(tk.Tk):
	def __init__(self, *args, **kwargs):
		
		tk.Tk.__init__(self, *args, **kwargs)
		
		container = tk.Frame(self)
		# container.pack(side = "top", fill = "both", expand = True)
		container.place(relx=0, rely=0)

		# container.grid_rowconfigure(0, weight = 1)
		# container.grid_columnconfigure(0, weight = 1)
		self.frames = {}
		for F in (StartPage, Page1, Page2):

			frame = F(container, self)
			self.frames[F] = frame

			frame.place(relx = 0, rely = 0)

		self.show_frame(StartPage)


	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()


class StartPage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="Startpage", font = LARGEFONT)
		label.place(relx=0.1, rely=0.1)
        # button1 = ttk.Button(self,text="Page 1",command=lambda:controller.show_frame(Page1))
		# button1.place(relx=0, rely=0.2)
        # button2 = ttk.Button(self, text = "Page 2", command = lambda : controller.show_frame(Page2))
		# button2.place(relx=0, rely=0.3)

		
class Page1(tk.Frame):
	
	def __init__(self, parent, controller):
		
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="Page 1", font = LARGEFONT)
		label.place(relx=0.1, rely=0.1)
		button1 = ttk.Button(self, text ="StartPage",command = lambda : controller.show_frame(StartPage))
		button1.place(relx=0, rely = 0.2)
		button2 = ttk.Button(self, text ="Page 2",command = lambda : controller.show_frame(Page2))
		button2.place(relx=0, rely = 0.3)


class Page2(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="Page 2", font = LARGEFONT)
		label.place(relx=0, rely=0.1)
		button1 = ttk.Button(self, text ="Page 1",command = lambda : controller.show_frame(Page1))
		button1.place(relx=0, rely = 0.2)
		# button2 = ttk.Button(self, text ="Startpage",command = lambda : controller.show_frame(StartPage))
		# button2.place(relx=0, rely = 0.3)


# Driver Code
app = tkinterApp()
app.mainloop()
