from tkinter import *
root = Tk()

i = Entry(root)
i.pack()

def myClick():
    hello = 'Hello ' + i.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()
    
    #fg = Font Color bg = background color, can be 'red'.. or hex numbers 
    # example bg = '#000000' for black color
myButton = Button(root, text='Click Me!', command=myClick, fg='red', bg='blue')
myButton.pack()

root.mainloop()