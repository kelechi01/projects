from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.geometry('800x550')
root.title('CHURCH MANAGEMENT SYSTEM')
bg = ImageTk.PhotoImage(Image.open('bg/bg2.PNG'))
label = Label(image=bg).place(relx=0, rely=0.06)
# bg2 = ImageTk.PhotoImage(Image.open('bg/logo.PNG'))
# label = Label(image=bg2).place(relx=0, rely=0.06)

main = LabelFrame(root, bg='#29292a',width=800, height=35).place(relx = 0, rely=0)


def home():


    # bg = ImageTk.PhotoImage(Image.open('bg/bg2.PNG'))
    # label = Label(image=bg).place(relx=0, rely=0.06)
    Label(root, text='The Apostolic',fg='white', bg='#49494c', 
            font=('ariel 20 bold')).place(relx=0.4, rely=0.45)
    Label(main, text='Church Management System',fg='white', 
            bg='#49494c', font=('ariel 20 bold')).place(relx=0.28, rely=0.52)
    Label(main, text='One fold, one shepherd...',fg='white', 
            bg='#49494c', font=('ariel', '12', 'bold italic')).place(relx=0.75, rely=0.94)




def signup():

    sign1_label = Label(main, text = 'First name',
        font=('ariel',10,'bold'),fg='white', bg='#9d35cf').place(relx=0.2, rely=0.13)

    sign1_entry = Entry(main, width=40,            
        font=('ariel',10,'bold'),fg='#9d35cf', bg='#f1e4ff').place(relx=0.2, rely=0.169)


    sign2_label = Label(main, text = 'Last name', 
        font=('ariel',10,'bold'),fg='white', bg='#9d35cf').place(relx=0.2, rely=0.269)

    sign2_entry = Entry(main, width=40, 
        font=('ariel',10,'bold'),fg='#9d35cf', bg='#f1e4ff').place(relx=0.2, rely=0.308)

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



Button(main, text='Home',width=10, font=('ariel 13 bold'), bg='#29292a', 
                fg='white', command=home).place(relx=0, rely =0)
Button(main, text='Sign up',width=10, font=('ariel 13 bold'), bg='#29292a',
                fg='white', command = signup).place(relx=0.13, rely =0)
Button(main, text='Login',width=10, font=('ariel 13 bold'), bg='#29292a', 
                fg='white').place(relx=0.26, rely =0)
Button(main, text='Anouncement',width=13, font=('ariel 13 bold'), bg='#29292a', 
                fg='white').place(relx=0.39, rely =0)





root.mainloop()