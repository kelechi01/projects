import tkinter as tk
from tkinter import ttk

# root.configure(bg='#ff9494')
# root.geometry('300x150')
# root.title('LOGIN')
# root.anchor('center')

# Label(root, text='Username',bg='#ff9494',font=('ariel 12 bold')).place(relx=0, rely=0.07)
# Entry(root,width=40,font=('ariel 10 bold')).place(relx=0, rely=0.23)

# Label(root, text='password',bg='#ff9494',font=('ariel 12 bold')).place(relx=0, rely=0.45)
# Entry(root,width=40,font=('ariel 10 bold')).place(relx=0, rely=0.6)

# Button(root, text='Login', fg='#ff9494', bg='black',font=('ariel 12 bold')).place(relx=0.4, rely=0.78)


# LARGEFONT = ('verdana', 35)
# class Project(tk.Tk):
#     def __init__(self, *args,**kwargs):
#         tk.Tk.__init__(self, *args,**kwargs)
#         container = tk.Frame(self)
#         container.place(relx=0,rely=0)
#         self.frames = {}
#         for F in (startpage, page1, page2):
#             frame = F(container, self)
#             self.frames[F] = frame
#             frame.place(relx=0, rely =0)
#         self.showframe(startpage)
#     def showframe(self, cont):
#         frame = self.frames[cont]
#         frame.tkraise()
# class startpage(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         label = ttk.Label(self, text='start page', font = LARGEFONT)
#         label.place(relx=0, rely=0.4)
#         button1= ttk.Button(self, text='page 1',command =lambda : controller.showframe(page1))
#         button1.place(relx=0.04, rely=0.2)
#         button2= ttk.Button(self, text='page 2')
#         command =lambda : controller.showframe(page2)
#         button1.place(relx=0.04, rely=0.3)
# class page1(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         label = ttk.Label(self, text='page 1', font = LARGEFONT)
#         label.place(relx=0, rely=0.4)
#         button1= ttk.Button(self, text='start page')
#         command =lambda : controller.showframe(page1)
#         button1.place(relx=0.04, rely=0.2)
#         button2= ttk.Button(self, text='page 2')
#         command =lambda : controller.showframe(page2)
#         button1.place(relx=0.04, rely=0.3)

# class page2(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         label = ttk.Label(self, text='page2', font = LARGEFONT)
#         label.place(relx=0, rely=0.4)
#         button1= ttk.Button(self, text='page 1')
#         command =lambda : controller.showframe(page1)
#         button1.place(relx=0.04, rely=0.2)
#         button2= ttk.Button(self, text='startpage')
#         command =lambda : controller.showframe(page2)
#         button1.place(relx=0.04, rely=0.3)
# app = Project()
# app.mainloop()



root = Tk()

login = tk.Frame(mainframe)

login_label = tk.Label(login, text = 'Email address', font = 10).pack(pady = 100)
login_entry = tk.Entry(login, width=30, font = 15)

login2_label = tk.Label(login, text = 'Password', font = 10)
login2_entry = tk.Entry(login, width=30, font = 15)

login_button = Button(login,text='Login', width=30, font = 15)






sign3_label = tk.Label(signup, text = 'Email', font = 10)
sign3_entry = tk.Entry(signup, width=30, font = 15)