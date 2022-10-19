import tkinter as tk
# from tkinter import ttk
from tkinter import *


# LARGEFONT =("Verdana", 35)

# class tkinterApp(tk.Tk):
	
# 	# __init__ function for class tkinterApp
# 	def __init__(self, *args, **kwargs):
		
# 		# __init__ function for class Tk
# 		tk.Tk.__init__(self, *args, **kwargs)
		
# 		# creating a container
# 		container = tk.Frame(self)
# 		container.pack(side = "top", fill = "both", expand = True)

# 		container.grid_rowconfigure(0, weight = 1)
# 		container.grid_columnconfigure(0, weight = 1)

# 		# initializing frames to an empty array
# 		self.frames = {}

# 		# iterating through a tuple consisting
# 		# of the different page layouts
# 		for F in (StartPage, Page1, Page2):

# 			frame = F(container, self)

# 			# initializing frame of that object from
# 			# startpage, page1, page2 respectively with
# 			# for loop
# 			self.frames[F] = frame

# 			frame.grid(row = 0, column = 0, sticky ="nsew")

# 		self.show_frame(StartPage)

# 	# to display the current frame passed as
# 	# parameter
# 	def show_frame(self, cont):
# 		frame = self.frames[cont]
# 		frame.tkraise()

# # first window frame startpage

# class StartPage(tk.Frame):
# 	def __init__(self, parent, controller):
# 		tk.Frame.__init__(self, parent)
		
# 		# label of frame Layout 2
# 		label = ttk.Label(self, text ="Startpage", font = LARGEFONT)
		
# 		# putting the grid in its place by using
# 		# grid
# 		label.grid(row = 0, column = 4, padx = 10, pady = 10)

# 		button1 = ttk.Button(self, text ="Page 1",
# 		command = lambda : controller.show_frame(Page1))
	
# 		# putting the button in its place by
# 		# using grid
# 		button1.grid(row = 1, column = 1, padx = 10, pady = 10)

# 		## button to show frame 2 with text layout2
# 		button2 = ttk.Button(self, text ="Page 2",
# 		command = lambda : controller.show_frame(Page2))
	
# 		# putting the button in its place by
# 		# using grid
# 		button2.grid(row = 2, column = 1, padx = 10, pady = 10)

		


# # second window frame page1
# class Page1(tk.Frame):
	
# 	def __init__(self, parent, controller):
		
# 		tk.Frame.__init__(self, parent)
# 		label = ttk.Label(self, text ="Page 1", font = LARGEFONT)
# 		label.grid(row = 0, column = 4, padx = 10, pady = 10)

# 		# button to show frame 2 with text
# 		# layout2
# 		button1 = ttk.Button(self, text ="StartPage",
# 							command = lambda : controller.show_frame(StartPage))
	
# 		# putting the button in its place
# 		# by using grid
# 		button1.grid(row = 1, column = 1, padx = 10, pady = 10)

# 		# button to show frame 2 with text
# 		# layout2
# 		button2 = ttk.Button(self, text ="Page 2",
# 							command = lambda : controller.show_frame(Page2))
	
# 		# putting the button in its place by
# 		# using grid
# 		button2.grid(row = 2, column = 1, padx = 10, pady = 10)




# # third window frame page2
# class Page2(tk.Frame):
# 	def __init__(self, parent, controller):
# 		tk.Frame.__init__(self, parent)
# 		label = ttk.Label(self, text ="Page 2", font = LARGEFONT)
# 		label.grid(row = 0, column = 4, padx = 10, pady = 10)

# 		# button to show frame 2 with text
# 		# layout2
# 		button1 = ttk.Button(self, text ="Page 1",
# 							command = lambda : controller.show_frame(Page1))
	
# 		# putting the button in its place by
# 		# using grid
# 		button1.grid(row = 1, column = 1, padx = 10, pady = 10)

# 		# button to show frame 3 with text
# 		# layout3
# 		button2 = ttk.Button(self, text ="Startpage",
# 							command = lambda : controller.show_frame(StartPage))
	
# 		# putting the button in its place by
# 		# using grid
# 		button2.grid(row = 2, column = 1, padx = 10, pady = 10)


# # # Driver Code
# # app = tkinterApp()
# # app.mainloop()





# def page1():
# 	pg2text.pack_forget()
# 	pg1text.pack()
# def page2():
# 	pg1text.pack_forget()
# 	pg2text.pack()


window = Tk()

# pg1btn = Button(window, text='page 1',command=page1)
# pg2btn = Button(window, text='page 2',command=page2)

# pg1text = Label(window, text='this is page1')
# pg2text = Label(window, text='this is page2')




# pg1btn.pack()
# pg2btn.pack()
# pg1text.pack()
# pg2text.pack()

# window.mainloop()



# root = Tk()
# root.geometry('700x400')
# root.title('CHURCH MANAGEMENT SYSTEM')


# mainframe = tk.Frame(root,)

# pg1 = tk.Frame(mainframe)
# pg1.pack(pady=100)

# pg1lb = tk.Label(pg1, text = 'start page', font=('bold', 20))
# pg1lb.pack()

# pg2 = tk.Frame(mainframe)
# pg2lb = tk.Label(pg2, text = 'home', font=('bold', 20))
# pg2lb.pack()

# pg3 = tk.Frame(mainframe)
# pg3lb = tk.Label(pg3, text = 'menu ', font=('bold', 20))
# pg3lb.pack()

# pg4 = tk.Frame(mainframe)
# pg4lb = tk.Label(pg4, text = 'about', font=('bold', 20))
# pg4lb.pack()

# mainframe.pack(fill=tk.BOTH, expand=True)

# pages = [pg1, pg2, pg3, pg4]
# count = 0

# def move_next_page():
# 	global count
# 	# count += 1
# 	if not count > len(pages)-2:
# 		for p in pages:
# 			p.pack_forget()
# 		count += 1
# 		page = pages[count]
# 		page.pack(pady = 100)



# def move_back_page():
# 	global count
	
# 	if not count == 0:
# 		for p in pages:
# 			p.pack_forget()
# 		count -= 1
# 		page = pages[count]
# 		page.pack(pady = 100)






# botton_frame = Frame(root)
# back_btn = Button(botton_frame, text='back',
# 				   font = ('bold', 12),
# 				   bg= '#1877f2', fg = 'white', width =8,
# 				   command = move_back_page)

# back_btn.pack(side = tk.LEFT, padx = 10)

# next_btn =Button(botton_frame, text='next',
# 				   font = ('bold', 12),
# 				   bg= '#1877f2', fg = 'white', width =8,
# 				   command = move_next_page)
# next_btn.pack(side = tk.RIGHT, padx = 10)


# botton_frame.pack(side = tk.BOTTOM, pady = 30)
# root.mainloop()


# ########################################################################################

# from tkinter import*
# import tkinter as tk
# # root = Tk()
# # root.geometry('700x400')
# # root.configure(bg='#9d35cf')
# # root.title('CHURCH MANAGEMENT SYSTEM')

# # Label(root, text='The Apostolic',fg='white', bg='#9d35cf', font=('ariel 20 bold')).place(relx=0.35, rely=0.35)
# # Label(root, text='Church Management System',fg='white', bg='#9d35cf', font=('ariel 20 bold')).place(relx=0.2, rely=0.44)

# # Button(root, text='Home',width=13, font=('ariel 15 bold'), bg='white', fg='#9d35cf').place(relx=0, rely =0)
# # Button(root, text='Sign up',width=13, font=('ariel 15 bold'), bg='white', fg='#9d35cf').place(relx=0.2, rely =0)
# # Button(root, text='Login',width=13, font=('ariel 15 bold'), bg='white', fg='#9d35cf').place(relx=0.4, rely =0)
# # Button(root, text='Anouncement',width=13, font=('ariel 15 bold'), bg='white', fg='#9d35cf').place(relx=0.6, rely =0)

# # def signup():
# #     logintext.pack_forget()
    

# # root.mainloop()





# root = Tk()
# root.geometry('700x400')
# root.title('CHURCH MANAGEMENT SYSTEM')


# mainframe = tk.Frame(root, bg='red')

# main = tk.Frame(mainframe)
# main.pack(pady=100)

# # main_label = tk.Label(pg1, text = 'start page', font=('bold', 20))
# # pg1.pack()
# main_label = tk.Label(main, text='The Apostolic',fg='white', bg='#9d35cf',
#                      font=('ariel 20 bold')).place(relx=0.35, rely=0.35)
# main_label2 = tk.Label(main, text='Church Management System',fg='white', bg='#9d35cf',
#                      font=('ariel 20 bold')).place(relx=0.2, rely=0.44)


# signup = tk.Frame(mainframe)

# sign1_label = tk.Label(signup, text = 'First name', font = 10).pack(pady = 100)
# sign1_entry = tk.Entry(signup, width=30, font = 15)

# sign2_label = tk.Label(signup, text = 'Last name', font = 10)
# sign2_entry = tk.Entry(signup, width=30, font = 15)

# sign3_label = tk.Label(signup, text = 'Email', font = 10)
# sign3_entry = tk.Entry(signup, width=30, font = 15)

# sign4_label = tk.Label(signup, text = 'Password (6 or more character)', font = 10)
# sign4_entry = tk.Entry(signup, width=30, font = 15)

# sign4_label = tk.Label(signup, text = 'Confirm password', font = 10)
# sign4_entry = tk.Entry(signup, width=30, font = 15)

# sign4_btn = tk.Button(signup, text='Join now', width=30)

# login = tk.Frame(mainframe)

# login_label = tk.Label(login, text = 'Email address', font = 10).pack(pady = 100)
# login_entry = tk.Entry(login, width=30, font = 15)

# login2_label = tk.Label(login, text = 'Password', font = 10)
# login2_entry = tk.Entry(login, width=30, font = 15)

# login_button = Button(login,text='Login', width=30, font = 15)


# # pg4 = tk.Frame(mainframe)
# # pg4lb = tk.Label(pg4, text = 'about', font=('bold', 20))
# # pg4lb.pack()

# mainframe.pack(fill=tk.BOTH, expand=True)

# pages = [main, signup, login]
# count = 0

# def move_next_page():
# 	global count
# 	# count += 1
# 	if not count > len(pages)-2:
# 		for p in pages:
# 			p.pack_forget()
# 		count += 1
# 		page = pages[count]
# 		page.pack(pady = 100)



# def move_back_page():
# 	global count
	
# 	if not count == 0:
# 		for p in pages:
# 			p.pack_forget()
# 		count -= 1
# 		page = pages[count]
# 		page.pack(pady = 100)






# botton_frame = Frame(root)
# sign_btn = Button(botton_frame, text='signup',
# 				   font = ('bold', 12),
# 				   bg= '#1877f2', fg = 'white', width =8,
# 				   command = move_back_page)

# sign_btn.pack(side = tk.LEFT, padx = 10)

# login_btn =Button(botton_frame, text='login',
# 				   font = ('bold', 12),
# 				   bg= '#1877f2', fg = 'white', width =8,
# 				   command = move_next_page)
# login_btn.pack(side = tk.RIGHT, padx = 10)


# botton_frame.pack(side = tk.TOP, pady = 30)

can
window.mainloop()


