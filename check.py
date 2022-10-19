
def check():
    a = sign5_entry.get()
    b = sign4_entry.get()
    if a == b:
        pass
    else:
        Label(main, text = 'incorrect password',
        font=('ariel',10,'bold'),fg='white', 
        bg='#9d35cf').place(relx=0.2, rely=0.94)
    if len(a) and len(b) <= 6:
        pass
    else:
        Label(main, text = 'weak password',
        font=('ariel',10,'bold'),fg='white', 
        bg='#9d35cf').place(relx=0.2, rely=0.94)
