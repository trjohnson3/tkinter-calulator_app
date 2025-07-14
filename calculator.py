from tkinter import *

root = Tk()
root.title("Calculator")

entryBox = Entry(root, width=35, borderwidth=5)
entryBox.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

temp_num = 0

def click_number(number):
    #entryBox.delete(0, END)
    entryBox.insert(END, number)

def click_clear():
    entryBox.delete(0, END)
    temp_num = 0

def click_add():
    if entryBox.get() == "":
        first_num = 0
    else:
        first_num = entryBox.get()
    global temp_num
    temp_num = int(first_num)
    entryBox.delete(0, END)

def click_equal():
    if entryBox.get() == "":
        second_num = 0
    else:
        second_num = entryBox.get()
    entryBox.delete(0, END)
    entryBox.insert(0, temp_num + int(second_num))

button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: click_number(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: click_number(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: click_number(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: click_number(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: click_number(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: click_number(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: click_number(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: click_number(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: click_number(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: click_number(0))
button_add = Button(root, text="+", padx=39, pady=20, command=click_add)
button_equal = Button(root, text="=", padx=91, pady=20, command=click_equal)
button_clear = Button(root, text="clear", padx=79, pady=20, command=click_clear)

#put buttons on screen

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)


root.mainloop()