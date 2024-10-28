from tkinter import *

root = Tk()
root.title('Simple Calculator')

e = Entry(root, text='1', padx=40, pady=20)

def button_add():
    pass

button_1 = Button(root, text='1', padx=40, pady=20, command=button_add)
button_2 = Button(root, text='2', padx=40, pady=20, command=button_add)
button_3 = Button(root, text='3', padx=40, pady=20, command=button_add)
button_4 = Button(root, text='4', padx=40, pady=20, command=button_add)
button_5 = Button(root, text='5', padx=40, pady=20, command=button_add)
button_6 = Button(root, text='6', padx=40, pady=20, command=button_add)
button_7 = Button(root, text='7', padx=40, pady=20, command=button_add)
button_8 = Button(root, text='8', padx=40, pady=20, command=button_add)
button_9 = Button(root, text='9', padx=40, pady=20, command=button_add)