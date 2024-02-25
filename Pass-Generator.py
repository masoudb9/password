from tkinter import *
import string
import random


def click():
    char = string.ascii_lowercase + string.ascii_uppercase + string.digits + '!@#$%'
    save = []
    for this in range(int(txt.get())):
        save.append(random.choice(char))
    x = ''.join(save)
    l1.insert(END, x)

def click2():
    l1.delete(END)


def click3():
    window.destroy()

window = Tk()
window.title("|^_^| Password Generator")
window.minsize(350, 210)
window.maxsize(350, 210)
Label(window, text="strong password generator".title(), background='gold', foreground='black',
      font=("Arial", 10, "bold")).pack(pady=5)
txt = Entry(window, background='lightgrey', foreground='black', width=50)
txt.pack(pady=5)
l1 = Listbox(window, height=1, width=50)
l1.pack(pady=5)
but = Button(window, text='Generate', background='green', foreground='black', command=click, font=("Arial", 10, "bold"),
             width=25)
but.pack(pady=5)
but2 = Button(window, text="Clear", background='red', foreground='black', font=("Arial", 10, "bold"),
              command=click2, width=25)
but2.pack(pady=5)
but3 = Button(window, text="Exit", background='grey', foreground='black', font=("Arial", 10, "bold"),
              command=click3, width=25)
but3.pack(pady=5)
window.mainloop()
