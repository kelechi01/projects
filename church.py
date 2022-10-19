from tkinter import *
top = Tk()
top.geometry('600x350')
# top.minsize(600, 350)
# top.maxsize(600, 350)
# top.resizable(0,0)

top['bg']='#f1e4ff'

main = LabelFrame(top, bg='#9d35cf',width=600, height=320).place(relx = 0, rely=0.1)


def home():

    main = LabelFrame(top, bg='#9d35cf',width=600, height=320).place(relx = 0, rely=0.1)

    Label(main, text='The Apostolic',fg='white', bg='#9d35cf', 
            font=('ariel 20 bold')).place(relx=0.35, rely=0.35)
    Label(main, text='Church Management System',fg='white', 
            bg='#9d35cf', font=('ariel 20 bold')).place(relx=0.2, rely=0.44)


def signup():
    main = LabelFrame(top, bg='#9d35cf',width=600, height=320).place(relx = 0, rely=0.1)

    sign1_label = Label(main, text = 'First name',
        font=('ariel',10,'bold'),fg='white', bg='#9d35cf').place(relx=0.2, rely=0.1)

    sign1_entry = Entry(main, width=40,            
        font=('ariel',10,'bold'),fg='#9d35cf', bg='#f1e4ff').place(relx=0.2, rely=0.169)


    sign2_label = Label(main, text = 'Last name', 
        font=('ariel',10,'bold'),fg='white', bg='#9d35cf').place(relx=0.2, rely=0.269)

    sign2_entry = Entry(main, width=40, 
        font=('ariel',10,'bold'),fg='#9d35cf', bg='#f1e4ff').place(relx=0.2, rely=0.338)

    sign3_label = Label(main, text = 'Email or Username',
        font=('ariel',10,'bold'),fg='white', bg='#9d35cf').place(relx=0.2, rely=0.438)

    sign3_entry = Entry(main, width=40, 
        font=('ariel',10,'bold'),fg='#9d35cf', bg='#f1e4ff').place(relx=0.2, rely=0.507)

    sign4_label = Label(main, text = 'Password (6 or more character)',
        font=('ariel',10,'bold'),fg='white', bg='#9d35cf').place(relx=0.2, rely=0.607)

    sign4_entry = Entry(main, width=40,
        font=('ariel',10,'bold'),fg='#9d35cf', bg='#f1e4ff',show='*').place(relx=0.2, rely=0.676)

    sign5_label = Label(main, text = 'Confirm password',
        font=('ariel',10,'bold'),fg='white', bg='#9d35cf').place(relx=0.2, rely=0.776)

    sign5_entry = Entry(main, width=40,
        font=('ariel',10,'bold'),fg='#9d35cf', bg='#f1e4ff',show='*').place(relx=0.2, rely=0.845)

    sign_btn = Button(main, text='Join now', width=10,
        font=('ariel',10,'bold'),fg='white', bg='#9d35cf').place(relx=0.76, rely=0.5)

def login():
    main = LabelFrame(top, bg='#9d35cf',width=600, height=320).place(relx = 0, rely=0.1)

    login_label = Label(main, text = 'Email address\nor Username ', 
        font=('ariel',10,'bold'),fg='white', bg='#9d35cf').place(relx=0.17, rely=0.28)
    login_entry = Entry(main, width=40, 
        font=('ariel',10,'bold'),fg='#9d35cf', bg='white').place(relx=0.35, rely=0.3)

    login2_label = Label(main, text = 'Password', 
        font=('ariel',10,'bold'),fg='white', bg='#9d35cf').place(relx=0.17, rely=0.45)
    login2_entry = Entry(main, width=40, 
        font=('ariel',10,'bold'),fg='#9d35cf', bg='white', show='*').place(relx=0.35, rely=0.45)

    login_button = Button(main,text='Login', width=30, 
        font=('ariel',10,'bold'),fg='white', bg='#9d35cf').place(relx=0.27, rely=0.63)





Button(top, text='Home',width=10, font=('ariel 13 bold'), bg='white', 
                fg='#9d35cf', command=home).place(relx=0, rely =0)
Button(top, text='Sign up',width=10, font=('ariel 13 bold'), bg='white',
                fg='#9d35cf',  command=signup).place(relx=0.2, rely =0)
Button(top, text='Login',width=10, font=('ariel 13 bold'), bg='white', 
                fg='#9d35cf', command=login).place(relx=0.4, rely =0)
Button(top, text='Anouncement',width=13, font=('ariel 13 bold'), bg='white', 
                fg='#9d35cf').place(relx=0.6, rely =0)


top.mainloop()