import tkinter as tk
from tkinter import *

root = Tk()
# sign1_label = tk.Label(signup, text = 'First name', font = 10).pack(pady = 100)
# sign1_entry = tk.Entry(signup, width=30, font = 15)

# sign2_label = tk.Label(signup, text = 'Last name', font = 10)
# sign2_entry = tk.Entry(signup, width=30, font = 15)

# sign3_label = tk.Label(signup, text = 'Email', font = 10)
# sign3_entry = tk.Entry(signup, width=30, font = 15)

# sign4_label = tk.Label(signup, text = 'Password (6 or more character)', font = 10)
# sign4_entry = tk.Entry(signup, width=30, font = 15)

# tk.Label(signup, text = 'Confirm password', font = 10)
# tk.Entry(signup, width=30, font = 15)

# tk.Button(signup, text='Join now', width=30)


ent = tk.Entry(root, width=40, bg='blue')
def btn():
    a = ent.get()
    print(a)


ent.place(relx=0.03, rely=0.1)
botton = tk.Button(root, width=10, bg='green', text='btn', command=btn).place(relx=0.1, rely=0.38)

root.mainloop()